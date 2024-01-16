import os
import csv

# Save file path to variable
budget_path = os.path.join("python-challenge", "PyBank", "resources", "budget_data.csv")

# Initialize variables
total_months = 0
net_total = 0
previous = 0
changes = []  # Change this to a list
dates = []

# Read file & set delimiter
with open(budget_path) as csvfile:
    budget_data = csv.reader(csvfile, delimiter=",")
    header = next(budget_data)  # Use budget_data instead of csvfile
    for row in budget_data:  # Use row instead of rows
        # The total number of months included in the dataset
        total_months += 1
        # The net total amount of "Profit/Losses" over the entire period
        net_total += int(row[1])
        # The changes in "Profit/Losses" over the entire period
        if total_months > 1:
            change = int(row[1]) - previous
            changes.append(change)  # Append changes to the list
            dates.append(row[0])  # Append dates to the list
        previous = int(row[1])

# Calculate the average change
average_change = sum(changes) / len(changes)

# The greatest increase in profits (date and amount) over the entire period
greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase)]

# The greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease)]

# Print the results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: {net_total}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")