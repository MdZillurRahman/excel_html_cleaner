# 🧹 Excel HTML Cleaner Web App

This is a simple Flask-based web app that lets you:

- Upload an Excel file (`.xlsx`)
- Specify a column (e.g., `holo.lists`)
- Automatically clean that column by:
  - Keeping only `<ul>` and `<ol>` blocks (and their inner content like `<li>`, `<a>`)
  - Removing everything else
- Download the cleaned file in seconds

---

## 💻 Requirements

- Python 3.8+
- Works on both **Mac** and **Windows**
- Recommended: use a virtual environment

---

## ⚙️ Setup Instructions

### 1. Clone or Download This Repo

```
git clone https://github.com/MdZillurRahman/excel_html_cleaner
cd excel_html_cleaner
```

### 2. Create Virtual Environment (Optional but Recommended)
## On Mac/Linux:
```
python3 -m venv .venv
source .venv/bin/activate
```

## On Windows:
```
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies
```
pip install flask pandas openpyxl beautifulsoup4
```

### 4. Run the App
```
python app.py
```

## How It Works
- Upload a .xlsx file.
- Enter the column name that contains HTML (e.g., holo.lists).
- The app keeps only `<ul>` and `<ol>` blocks (and anything inside them like `<li>`, `<a>`).
- Everything else is removed.
- The cleaned file is automatically generated and available for download.