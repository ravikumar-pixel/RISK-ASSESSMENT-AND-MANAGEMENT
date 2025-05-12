def calculate_risk_score(probability, impact, detectability):
    score = probability * impact * detectability
    if score >= 150:
        level = "High Risk"
    elif score >= 50:
        level = "Medium Risk"
    else:
        level = "Low Risk"
    return score, level

if __name__ == "__main__":
    probability = 5
    impact = 7
    detectability = 4
    score, level = calculate_risk_score(probability, impact, detectability)
    print(f"Risk Score: {score} ({level})")
