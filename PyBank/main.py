# PyBank --- Python Challenge

# Import os and csv modules
import os
import csv
  
# Initialize variables
budget_data = []
output_data = ""
total_months = 0
total_amount = 0
average_change = []
change = 0

# Following variables store the data for greatest increase/decrease
inc_amt = 0
inc_month = ""
dec_amt = 0
dec_month = ""

# opening the csv
filepath = os.path.join('Resources','budget_data.csv')
with open(filepath) as csvfile:

    csv_reader = csv.reader(csvfile)
    colunns = next(csv_reader)
    row1 = next(csv_reader)
    total_months += 1 
    previous_pl = int(row1[1])
    total_amount = int(row1[1])

    # looping through the budget_data
    for row in csv_reader:
        total_months += 1 
        total_amount += int(row[1])
        current_pl = int(row[1]) 
        change = (current_pl - previous_pl)
        average_change.append(change)
        previous_pl = int(row[1])

        if inc_amt < change:
            inc_amt = change
            inc_month = row[0]

        if dec_amt > change:
            dec_amt = change
            dec_month = row[0]
   
    average = round((sum(average_change)/len(average_change)),2)

# Create a .txt file to contain the vote analysis
write_file = os.path.join('analysis', 'financial_analysis.txt')
filewriter = open(write_file, mode = 'w')

# Print analysis to file
filewriter.write(" \n")
filewriter.write("Financial Analysis\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Months: {total_months}\n")
filewriter.write(f"Total: ${total_amount:,.0f}\n")
filewriter.write(f"Average Change: ${average:,.2f}\n")
filewriter.write(f"Greatest Increase in Profits: {inc_month} (${inc_amt:,.0f})\n")
filewriter.write(f"Greatest Decrease in Profits: {dec_month} (${dec_amt:,.0f})\n")
filewriter.write(" \n")

# Close output file
filewriter.close()

# Display output on terminal
with open(write_file, 'r') as f:
    print(f.read())
