# scanner/risk_scorer.py

def calculate_risk_score(findings: dict) -> int:
    """
    Assigns a risk score based on the type and amount of sensitive data found.
    Range: 0 (no risk) to 100 (high risk)
    """
    score = 0
    weights = {
        "Email": 5,
        "Phone": 5,
        "PAN": 10,
        "Aadhaar": 10
    }
    for key, matches in findings.items():
        weight = weights.get(key, 1)
        score += len(matches) * weight

    return min(score, 100)
