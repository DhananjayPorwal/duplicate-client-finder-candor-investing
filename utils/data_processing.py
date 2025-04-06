import pandas as pd

def clean_data(df, source):
    """Cleans the given dataframe based on source."""
    df.columns = df.columns.str.strip().str.upper()
    
    column_mapping = {
        "RIA": {"PAN NO": "PAN", "D.O.B.": "DOB"},
        "Mutual Funds": {"CLIENT": "NAME"},
        "Smallcase": {}
    }
    
    if source in column_mapping:
        df.rename(columns=column_mapping[source], inplace=True)
    
    required_columns = ["NAME", "PAN", "DOB"]
    df = df[[col for col in required_columns if col in df.columns]]
    
    if "PAN" not in df.columns:
        raise KeyError(f"No PAN column found in {source} data. Columns found: {df.columns.tolist()}")
    
    # Strip whitespace from all columns to avoid issues
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Replace empty strings with NaN to handle them as missing values
    df.replace("", float('nan'), inplace=True)
    
    # Remove rows with missing values in Name, PAN, or DOB
    df = df.dropna(subset=["NAME", "PAN", "DOB"], how='any')
    
    df["PAN"] = df["PAN"].astype(str).str.upper().str.strip()
    
    # Convert DOB to consistent format
    df["DOB"] = pd.to_datetime(df["DOB"], errors='coerce').dt.strftime('%d-%m-%Y')
    df["Source"] = source
    return df

def process_files(files_dict):
    """Processes the files and finds common PAN numbers."""
    cleaned_dfs = []
    
    for source, df in files_dict.items():
        try:
            cleaned_dfs.append(clean_data(df, source))
        except KeyError as e:
            raise ValueError(f"Invalid file format for {source}: {str(e)}")
    
    combined_df = pd.concat(cleaned_dfs, ignore_index=True)
    
    if "PAN" not in combined_df.columns:
        raise ValueError("❌ PAN column missing in the merged data. Check input files.")

    pan_counts = combined_df["PAN"].value_counts()
    common_pans = pan_counts[pan_counts > 1].index.tolist()
    
    result_df = combined_df[combined_df["PAN"].isin(common_pans)]
    
    # Ensure only Name, PAN, and DOB are shown in final output
    return result_df[["NAME", "PAN", "DOB"]]
