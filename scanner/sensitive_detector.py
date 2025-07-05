# scanner/sensitive_detector.py
import re

# Basic sensitive data patterns (extendable)
patterns = {
    "Email": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    "Phone": r'(\+91[\-\s]?)?[789]\d{9}',
    "PAN": r'[A-Z]{5}[0-9]{4}[A-Z]',
    "Aadhaar": r'\d{4} \d{4} \d{4}'
}

def detect_sensitive_data(file_path):
    findings = {}
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            for label, pattern in patterns.items():
                matches = re.findall(pattern, content)
                if matches:
                    findings[label] = matches
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return findings
