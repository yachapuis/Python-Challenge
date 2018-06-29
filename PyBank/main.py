# main.py
# PyBank
#
# ------------------------------------------
#  Require Dependencies
# ------------------------------------------
# Modules
import os
import csv  
#
# ------------------------------------------
#  CSV Files
# ------------------------------------------
# Set path for file
csv_path = os.path.join("budget_data.csv")
txt_output = os.path.join("analysis", "election_analysis.txt")  
# 
# ------------------------------------------
# Main
# ------------------------------------------
# Variables
number_months = 0
total_revenue = 0
change_revenue = 0
revenue_memory = 0
change_revenue_list = []
average_change = 0
# month_change = []
top_benefit = ["", 0]
top_losses = ["", 9999999999999999999]

# Read the csv file and convert it into lists
with open(csv_path) as budget_data:
    csv_reader = csv.reader(budget_data)

    # Skip first row
    next(csv_reader) 

# Extract first row to avoid appending to net_change_list
#   first_row = next(reader)
#   total_months = total_months + 1
#   total_net = total_net + int(first_row[1])
#   prev_net = int(first_row[1])

    # Loop
    for row in csv_reader:

        # Count months number and total of revenue
        number_months = number_months + 1
        total_revenue = total_revenue + int(row[1])
       
        # Calculate change of revenue between months
        change_revenue = int(row[1]) - revenue_memory
        revenue_memory = int(row[1])
        change_revenue_list = change_revenue_list.append(change_revenue)

        # Calculate the greatest increase in profits (date and amount) over the entire period
        if change_revenue > top_benefit[1]:
            top_benefit[1] = change_revenue
            top_benefit[0] = row[0]

         # Calculate greatest decrease in losses (date and amount) over the entire period
        if change_revenue < top_losses[1]:
            top_losses[1] = change_revenue
            top_losses[0] = row[0]

# Calculate the average change in revenue between months over the entire period
average_change = sum(change_revenue_list) / len(change_revenue_list)

# ------------------------------------------
# Output
# ------------------------------------------
# Generate Table for Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Number of Months: {number_months}\n"
    f"Total Amount of Revenue: ${total_revenue}\n"
    f"Average Change in Revenue: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {top_profit[0]} (${top_profit[1]})\n"
    f"Greatest Decrease in Profits: {top_losses[0]} (${top_losses[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
