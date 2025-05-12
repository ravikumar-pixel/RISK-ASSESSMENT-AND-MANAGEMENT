import matplotlib.pyplot as plt

# Risk levels and their counts
risk_levels = ['Low', 'Medium', 'High']
counts = [5, 4, 1]  # Adjust these values based on actual data

# Corresponding colors for each bar
colors = ['red', 'orange', 'green']

# Create the bar chart
plt.bar(risk_levels, counts, color=colors)

# Add title and labels
plt.title('Risk Levels Distribution')
plt.xlabel('Risk Level')
plt.ylabel('Number of Risks')

# Display the plot
plt.show()
