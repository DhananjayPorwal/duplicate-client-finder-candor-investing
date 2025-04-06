import streamlit as st
import pandas as pd
from utils.data_processing import process_files, clean_data



# Streamlit Configuration
    
st.set_page_config(page_title="PAN Number Matching App", page_icon="logox.png", menu_items={
        'Get Help': 'https://github.com/DhananjayPorwal/duplicate-client-finder-candor-investing/blob/main/README.md',
        'Report a bug': "mailto:dporwal985@gmail.com",
        'About': "### Created by [Candor Investing](https://www.candorinvesting.com/)"
    }, layout="wide")

# Load the custom CSS from an external file
def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Use the function to load the CSS
load_css()

def main():


    # Add company logo
    logo_path = "candor_investing_logo.png"  # Ensure this logo file is in the same directory as this script
    st.image(logo_path, width=150)  # You can adjust the width as needed

    # st.set_page_config(page_title="PAN Number Matching App", layout="wide")

    st.markdown("""
    <h1 style='text-align: center;'>🔍 PAN Number Matching App</h1>
    <h3 style='text-align: center;'>Upload your files below to check for common PAN numbers across datasets.</h3>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        ria_file = st.file_uploader("📂 Upload RIA Excel File", type=["xlsx"])
    with col2:
        mf_file = st.file_uploader("📂 Upload Mutual Funds CSV File", type=["csv"])
    with col3:
        sc_file = st.file_uploader("📂 Upload Smallcase CSV File", type=["csv"])
    
    valid_files = {}
    uploaded_files = {"RIA": ria_file, "Mutual Funds": mf_file, "Smallcase": sc_file}
    
    for name, file in uploaded_files.items():
        if file:
            try:
                if name == "RIA":
                    df = pd.read_excel(file)
                else:
                    df = pd.read_csv(file)
                df = clean_data(df, name)
                valid_files[name] = df
            except Exception as e:
                st.error(f"❌ Error processing {name}: {str(e)}")
                return
    
    # Display Stats for Uploaded Files in Parallel
    if valid_files:
        st.markdown("### 📊 Uploaded File Statistics")
        stats_cols = st.columns(len(valid_files))
        
        for idx, (name, df) in enumerate(valid_files.items()):
            with stats_cols[idx]:
                st.markdown(f"#### {name}")
                st.write(f"- **Total Clients (After Cleaning):** {df.shape[0]}")
                selected_columns = [col for col in ["Name", "PAN", "DOB"] if col in df.columns]
                st.dataframe(df[selected_columns], height=200, use_container_width=True)
    
    st.markdown("""<div style='text-align: center;'>""", unsafe_allow_html=True)
    process_btn = st.button("🚀 Process Files")
    st.markdown("""</div>""", unsafe_allow_html=True)
    
    if process_btn:
        if len(valid_files) < 2:
            st.warning("⚠️ Please upload at least two valid files.")
            return
        
        result_df = process_files(valid_files)
        
        if result_df.empty:
            st.info("✅ No duplicate PAN entries found across the uploaded files.")
            st.balloons()
        else:
            result_df = result_df.drop_duplicates(subset=["PAN"])
            st.write("### 🎯 Matching PAN Entries")
            selected_columns = [col for col in ["Name", "PAN", "DOB", "Mobile Number", "Email"] if col in result_df.columns]
            st.dataframe(result_df[selected_columns], height=200, use_container_width=True)
            st.snow()

if __name__ == "__main__":
    main()



# MARK: FOOTER

footer="""<style>
a:link , a:visited{
color: #075e54;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #dcf8c6;
color: #128c7e;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with 💖 by <a href="https://candorinvesting.com/">Candor Investing</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
