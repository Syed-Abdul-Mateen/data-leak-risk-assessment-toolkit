# main.py

from scanner.file_scanner import scan_directory
from scanner.sensitive_detector import detect_sensitive_data
from scanner.risk_scorer import calculate_risk_score
from reporter.report_generator import export_to_csv, export_to_pdf
from reporter.cli_display import display_file_result, display_summary

def main():
    print("=== Data Leak Risk Assessment Toolkit ===")
    path = input("Enter the full directory path to scan: ").strip()

    file_paths = scan_directory(path, extensions=[".txt", ".log", ".csv"])
    if not file_paths:
        print("No matching files found.")
        return

    report_data = []

    for file in file_paths:
        findings = detect_sensitive_data(file)
        if findings:
            score = calculate_risk_score(findings)
            report_data.append({
                "file": file,
                "findings": findings,
                "score": score
            })
        display_file_result(file, findings, calculate_risk_score(findings) if findings else 0)

    display_summary(report_data)

    if report_data:
        export_to_csv(report_data)
        export_to_pdf(report_data)

if __name__ == "__main__":
    main()
