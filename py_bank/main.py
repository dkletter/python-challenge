# 1. total number of months in the dataset
# 2. net total amount of "Profit/Losses" over the entire period
# 3. calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# 4. greatest increase in profits (date and amount) over the entire period
# 5. greatest decrease in profits (date and amount) over the entire period
# 6. print the analysis to the terminal and export results to a text file

# Import modules
import os
import csv

# Path to collect data from the resources folder
input_path = os.path.join('resources', 'budget_data.csv')
output_path = os.path.join('analysis', 'pnl_analysis.txt')

# Create lists to store data
revenue_changes = []

# Initialize variables
total_months = 0
total_revenue = 0
prev_revenue = 0
revenue_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]

# Open and read csv
with open(input_path, 'r', encoding='utf8') as pnl_file:
    pnl_reader = csv.reader(pnl_file, delimiter=',')

    # Read the header row first
    pnl_header = next(pnl_reader)

    # Read through each row of data after the header
    for row in pnl_reader:

        # Calculate totals
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])
  
        # Keep track of changes
        revenue_change = int(row[1]) - prev_revenue
   
        # Reset the value of prev_revenue
        prev_revenue = int(row[1])
    
        # Determine greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row[0]

        # Determine greatest decrease
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row[0]

        # Add to the revenue_changes list
        revenue_changes.append(int(row[1]))

    # Calculate the average
    # revenue_avg = sum(revenue_changes) / len(revenue_changes)
    
    # Print output
    print()
    print()
    print()
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + "$" + str(total_revenue))
    print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes), 2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")

# Write output
with open(output_path, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes), 2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")