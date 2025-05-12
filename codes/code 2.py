risks = [
    {'id': 'R1', 'likelihood': 'High', 'impact': 'High'},
    {'id': 'R2', 'likelihood': 'Medium', 'impact': 'High'},
    {'id': 'R3', 'likelihood': 'High', 'impact': 'Medium'}
]

for risk in risks:
    if risk['likelihood'] == 'High' and risk['impact'] == 'High':
        print(f"{risk['id']} is Critical")
    elif risk['impact'] == 'High':
        print(f"{risk['id']} is High")
    else:
        print(f"{risk['id']} is Medium")
