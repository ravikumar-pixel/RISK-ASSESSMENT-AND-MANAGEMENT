# Define the list of risks
risks = [
    {"name": "Data breach", "likelihood": 5, "impact": 5},
    {"name": "Power failure", "likelihood": 3, "impact": 4},
    {"name": "Employee error", "likelihood": 4, "impact": 2},
    {"name": "Market fluctuation", "likelihood": 2, "impact": 3}
]

# Define the risk assessment function
def assess_risks(risks):
    print("RISK ASSESSMENT REPORT")
    print("-" * 40)
    for risk in risks:
        score = risk["likelihood"] * risk["impact"]
        if score >= 20:
            treatment = "Avoid or Mitigate"
        elif score >= 10:
            treatment = "Mitigate or Transfer"
        else:
            treatment = "Accept or Monitor"
        
        print(f"Risk: {risk['name']}")
        print(f" Likelihood: {risk['likelihood']} (1-5)")
        print(f" Impact: {risk['impact']} (1-5)")
        print(f" Risk Score: {score}")
        print(f" Suggested Treatment: {treatment}")
        print("-" * 40)

# Run the risk assessment
assess_risks(risks)
