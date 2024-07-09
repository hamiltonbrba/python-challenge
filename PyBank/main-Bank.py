# import modules (os, csv, statistics)
import os
import csv
import statistics


# Path to the budget CSV file, output folder for financial analysis text file
csv_file_path = os.path.join('Resources', 'budget_data.csv')
output_folder = 'analysis'
output_file_path = os.path.join(output_folder, 'financial_analysis.txt')

# Initialize variables - keep track of total months, net total profits/losses, and list of changes
total_months = 0
net_total = 0
changes = []
months = []

# Read the CSV File - read the content, skip header, track previous month's profit/loss
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) # Skip the header row
    prev_row = next(csv_reader)

    total_months += 1
    net_total += int(prev_row[1])
    prev_profit_loss = int(prev_row[1])

    for row in csv_reader:
        total_months += 1
        net_total += int(row[1])

        # Calculate Change
        change = int(row[1]) - prev_profit_loss
        changes.append(change)
        months.append(row[0])

        # Update previous row's profit/loss
        prev_profit_loss = int(row[1])

# Calculate average change (added if/else to clearly define average change) 
if changes:
    average_change = statistics.mean(changes)
else:
    average_change = 0

# Find greatest increase and decrease in profits
greatest_inc = max(changes)
greatest_dec = min(changes)
greatest_inc_month = months[changes.index(greatest_inc)]
greatest_dec_month = months[changes.index(greatest_dec)]

# Print Results with formatting considerations
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})")
print(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})")

# Export results to text file
with open(output_file_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})\n")
