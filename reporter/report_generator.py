# reporter/report_generator.py

import csv
from fpdf import FPDF
import os

def export_to_csv(report_data, output_path="output/report.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["File Path", "Sensitive Data Found", "Risk Score"])
        for item in report_data:
            writer.writerow([item["file"], str(item["findings"]), item["score"]])
    print(f"CSV report saved to: {output_path}")


class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 14)
        self.cell(0, 10, "Data Leak Risk Assessment Report", ln=True, align="C")

    def add_file_entry(self, file, findings, score):
        self.set_font("Arial", '', 11)
        self.multi_cell(0, 10, f"File: {file}\nRisk Score: {score}\nFindings: {findings}\n", border=0)

def export_to_pdf(report_data, output_path="output/report.pdf"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pdf = PDFReport()
    pdf.add_page()

    for item in report_data:
        pdf.add_file_entry(item["file"], item["findings"], item["score"])

    pdf.output(output_path)
    print(f"PDF report saved to: {output_path}")
