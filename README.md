# Data Leak Risk Assessment Toolkit 

A Python-based cybersecurity tool that scans directories for potential data leaks, detects sensitive information (like emails, PAN numbers, phone numbers, Aadhaar), calculates a risk score, and generates professional CSV + PDF reports. Built for security analysts, system auditors, and researchers.

---

##  Features

- Recursive directory scanning
- Pattern-based sensitive data detection
- Customizable regex (Email, PAN, Aadhaar, Phone)
- Risk scoring engine (0–100)
- Terminal-based summary (with color highlighting)
- Exportable PDF and CSV reports
- Easy to extend and test
- Built entirely in Python

---

##  Folder Structure

```
data-leak-risk-assessment-toolkit/
├── main.py
├── scanner/
│   ├── file_scanner.py
│   ├── sensitive_detector.py
│   ├── risk_scorer.py
├── reporter/
│   ├── report_generator.py
│   ├── cli_display.py
├── tests/
│   ├── __init__.py
│   ├── test_scanner.py
├── output/
│   ├── report.csv
│   ├── report.pdf
├── requirements.txt
├── README.md
```

---

## 🛠 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/Syed-Abdul-Mateen/data-leak-risk-assessment-toolkit
   cd data-leak-risk-assessment-toolkit
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the scanner:
   ```bash
   python main.py
   ```

---

##  Run Tests

```bash
python -m unittest discover -s tests
```

---

##  Sample Output

| File           | Score | Findings              |
|----------------|-------|------------------------|
| `data.txt`     | 85    | Email: 2, PAN: 1       |
| `logfile.log`  | 40    | Aadhaar: 1             |
| `user.csv`     | 0     | None                   |

---

##  Use Cases

- Detect exposed sensitive data in uploaded folders
- Run before uploading logs to third-party servers
- Automate leak scans on endpoints or servers
- Pair with DLP tools as a custom scanner

---

##  Author

**Syed Abdul Mateen**  
Final-Year B.Tech CSE | ICFAI Tech Hyderabad  
🔗 [GitHub Profile](https://github.com/Syed-Abdul-Mateen)

---

##  Show Your Support

If you found this useful, leave a ⭐ on the repo. It really helps!
