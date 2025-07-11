from flask import Flask, render_template, request, send_file, redirect, url_for
from bs4 import BeautifulSoup
import pandas as pd
import os
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def clean_html(html):
    if pd.isna(html):
        return html

    soup = BeautifulSoup(html, "html.parser")
    allowed_blocks = soup.find_all(["ul", "ol"])
    return "".join(str(tag) for tag in allowed_blocks)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files["excel_file"]
        column_name = request.form.get("column_name", "").strip()

        if not uploaded_file or not column_name:
            return "Please upload a file and enter a column name."

        # Save uploaded file
        file_id = uuid.uuid4().hex
        file_path = os.path.join(UPLOAD_FOLDER, f"{file_id}.xlsx")
        uploaded_file.save(file_path)

        try:
            df = pd.read_excel(file_path)
        except Exception as e:
            return f"Failed to read Excel file: {e}"

        if column_name not in df.columns:
            return f"Column '{column_name}' not found. Available columns: {', '.join(df.columns)}"

        df[column_name] = df[column_name].apply(clean_html)

        output_path = os.path.join(OUTPUT_FOLDER, f"{file_id}_cleaned.xlsx")
        df.to_excel(output_path, index=False)

        return redirect(url_for("download", filename=os.path.basename(output_path)))

    return render_template("index.html")

@app.route("/download/<filename>")
def download(filename):
    return send_file(os.path.join(OUTPUT_FOLDER, filename), as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
