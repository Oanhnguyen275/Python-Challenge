# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
average_change=[]
changes=[]
greatest_increase=["",float('-Inf')]
greatest_decrease=["",float('Inf')]
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)

    # Track the total and net change
    total_months += 1
    previous_revenue = int(first_row[1])
    total_net += previous_revenue

    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1
        profit_loss = int(row[1])
        total_net += profit_loss

        # Track the net change
        average_change = profit_loss - previous_revenue
        previous_revenue = int(row[1])
        changes.append(average_change)
        # Calculate the greatest increase in profits (month and amount)
        if average_change > greatest_increase[1]:
            greatest_increase = (row[0], average_change)

        # Calculate the greatest decrease in losses (month and amount)
        if average_change<greatest_decrease[1]:
            greatest_decrease=(row[0],average_change)

# Calculate the average net change across the months
average_change=sum(changes)/len(changes)

# Generate the output summary
output_summary=(
f"\nFinancialAnalysis"
"\n----------------------"
f"\nTotalMonths: {total_months}"
f"\nTotal: ${total_net}"
f"\nAverageChange: ${average_change}"
f'\nGreatestIncrease: {greatest_increase[0]} (${greatest_increase[1]})'
f"\nGreatestDecrease: {greatest_decrease[0]} (${greatest_decrease[1]})"
)

# Print the output
print(output_summary)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output_summary)
