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
txt_output = os.path.join("election_analysis.txt")  
# 
# ------------------------------------------
# Main
# ------------------------------------------
# Initiate variable value
number_months = 0
total_revenue = 0
change_revenue = 0
revenue_memory = 0
average_change = 0
# Initiate variable list
change_revenue_list = []
top_profit_list = ["", 0]
top_losses_list = ["", 9999999999999999999]

# Read the csv file and convert it into lists
with open(csv_path) as budget_data:
    csv_reader = csv.reader(budget_data)

    # Skip the first row of the csv_reader file
    next(csv_reader) 

    # Read all rows of the csv_reader file in a loop
    for row in csv_reader:

        # Count months number and total of revenue
        number_months = number_months + 1
        total_revenue = total_revenue + int(row[1])
       
        # Calculate change of revenue between months
        change_revenue = int(row[1]) - revenue_memory
        revenue_memory = int(row[1])
        change_revenue_list.append(change_revenue)

        # Calculate the greatest increase in profits (date and amount) over the entire period
        if change_revenue > top_profit_list[1]:
            top_profit_list[1] = change_revenue
            top_profit_list[0] = row[0]

         # Calculate greatest decrease in losses (date and amount) over the entire period
        if change_revenue < top_losses[1]:
            top_losses_list[1] = change_revenue
            top_losses_list[0] = row[0]

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
    f"Greatest Increase in Profits: {top_profit_list[0]} (${top_profit_list[1]})\n"
    f"Greatest Decrease in Profits: {top_losses_list[0]} (${top_losses_list[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(txt_output, "w") as txt_file:
    txt_file.write(output)
