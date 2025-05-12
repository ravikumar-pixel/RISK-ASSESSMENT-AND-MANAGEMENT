import csv

def add_risk(description, probability, impact):
    risk_score = probability * impact
    level = "High" if risk_score > 70 else "Medium" if risk_score > 30 else "Low"
    
    with open("risk_register.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([description, probability, impact, risk_score, level])
    
    print("Risk added successfully!")

if __name__ == "__main__":
    add_risk("Data breach vulnerability", 9, 8)
