import os  
import csv

# Save file path to variable
budget_path = os.path.join("python-challenge", "PyBank", "resources", "budget_data.csv")

# Initialize variables
total_months = 0
net_total = 0
previous = 0
changes = []
dates = []


# Read file & set delimeter
with open(budget_path) as csvfile:
    budget_data = csv.reader(csvfile, delimiter= ",")
    # how to get it to read Header? "next(csv_reader)"
    header = next(csvfile)
    # Loop through the data file
    for rows in budget_data:

        # The total number of months included in the dataset
        total_months = total_months + 1
        
        # The net total amount of "Profit/Losses" over the entire period /// Given help on the +=
        net_total += int(rows[1])

        # The changes in "Profit/Losses" over the entire period //// Given help on 4 of these - would like explaining
        if total_months > 1:
            change = int(rows[1]) - previous  # connecting to line 34
            changes.append(change)  # Append changes to the list
            dates.append(rows[0])  # Append dates to the list
        previous = int(rows[1])
        
    print(changes)
    print(dates)
    # Calculate the average change
    average_change = sum(changes) / len(changes)

    # The greatest increase in profits (date and amount) over the entire period //// given help on part 2
    greatest_increase = max(changes)
    greatest_increase_date = dates[changes.index(greatest_increase)]

    # The greatest decrease in profits (date and amount) over the entire period //// given help on part 2
    greatest_decrease = min(changes)
    greatest_decrease_date = dates[changes.index(greatest_decrease)]


 # Print the results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: {net_total}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")  # given help here
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")  # given help here