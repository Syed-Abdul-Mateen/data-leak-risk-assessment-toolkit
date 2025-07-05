# tests/test_scanner.py

import os
import tempfile
import unittest

from scanner.file_scanner import scan_directory
from scanner.sensitive_detector import detect_sensitive_data
from scanner.risk_scorer import calculate_risk_score

class TestScannerModules(unittest.TestCase):
    def test_file_scanning_and_detection(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            test_file_path = os.path.join(tmpdir, "test.txt")
            with open(test_file_path, "w") as f:
                f.write("My email is example@example.com\nPAN: ABCDE1234F")

            files = scan_directory(tmpdir, extensions=[".txt"])
            self.assertEqual(len(files), 1)
            self.assertIn(test_file_path, files)

            findings = detect_sensitive_data(test_file_path)
            self.assertIn("Email", findings)
            self.assertIn("PAN", findings)

            score = calculate_risk_score(findings)
            self.assertGreater(score, 0)

if __name__ == "__main__":
    unittest.main()
