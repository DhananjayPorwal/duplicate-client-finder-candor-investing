# 🔍 PAN Number Matching App

This tool helps you quickly check for **duplicate PAN numbers** across different client datasets — such as **RIA Excel files**, **Mutual Fund CSVs**, and **Smallcase CSVs** — with a simple file upload process. No coding knowledge required!

---

## 🚀 What does this app do?

This app helps you:
- ✅ Upload and clean your client data files.
- 🔍 Identify **duplicate PAN numbers** across the uploaded files.
- 📊 View a summary and filtered results instantly on the screen.

It’s fast, private (everything happens in your browser), and built with 💖 to save you time!

---

## 📁 Supported Files

You can upload files in the following formats:
- **RIA File:** Excel format (.xlsx)
- **Mutual Fund File:** CSV format (.csv)
- **Smallcase File:** CSV format (.csv)

Each file should contain client details such as **Name**, **PAN Number**, and **Date of Birth (DOB)**.

---

## 🧑‍💻 How to Use

1. ✅ Open the web app (hosted link or run locally — see below).
2. 📂 Upload your **RIA**, **Mutual Fund**, and **Smallcase** files.
3. 🔍 Click on **"Process Files"** to find duplicate PANs.
4. 🎯 View the matching records instantly on screen.
5. 🎉 If no duplicates are found, we’ll celebrate with you!

---

## 🖥️ How to Run the App Locally (For Tech Users)

> If you're a bit technical and want to run it yourself, follow these steps:

### Prerequisites
- Install Python 3.10+
- Install pip (Python package manager)

### 1. Clone the Repository
```bash
git clone https://github.com/DhananjayPorwal/duplicate-client-finder-candor-investing.git
cd duplicate-client-finder-candor-investing
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App
```bash
streamlit run app.py
```

---

## 📂 Folder Structure

```
pan-matching-app/
├── app.py                      # Main Streamlit app
├── candor_investing_logo.png  # Company logo
├── logox.png                  # Favicon/logo for tab
├── Procfile                   # Deployment config (e.g., Heroku)
├── README.md                  # You're reading it!
├── requirements.txt           # Python dependencies
├── runtime.txt                # Python version for deployment
├── styles.css                 # Custom styling for app
└── utils/
    ├── data_processing.py     # Logic for data cleaning and matching
```

---

## 🧼 How Does Data Cleaning Work?

Before finding duplicates, the app:
- Standardizes column names (like `PAN NO` → `PAN`)
- Removes extra spaces and empty values
- Converts dates to a consistent format
- Filters out rows missing important details

This ensures accurate and fair PAN matching.

---

## 🧠 Tech Stack

- **Python** 🐍
- **Pandas** for data processing
- **Streamlit** for UI
- **Deployed with:** Heroku (optional)

---

## 👨‍💼 Created By

Made with 💖 by [Candor Investing](https://www.candorinvesting.com/)
