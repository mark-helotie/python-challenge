# PyBank --- Python Challenge

# Import os and csv modules
import os
import csv

# Initialize variables
months = []
profitloss = []

# Set path for the input file
input_path = os.path.join('Resources', 'budget_data.csv')

# Open the CSV
with open(input_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    skipheader = next(csvreader)

    # Loop through the CSV
    for row in csvreader:
    
        # Add date
        months.append(row[0])
        
        # Add Profit/Loss
        profitloss.append(float(row[1]))

# Calculate the total months
totalmonths = (len(months))

# Calculate the net total amount
totalamount = sum(profitloss)

# Calculate the average change per month
avgchange = totalamount / totalmonths

# Calculate the greatest increase
maxprofit = max(profitloss)

# Use the index of the greatest increase to find the corresponding date
indexmax = profitloss.index(maxprofit)
maxmonth = months[indexmax]

# Calculate the greatest decrease 
minprofit = min(profitloss)

# Use the index of the greatest decrease to find the corresponding date
indexmin = profitloss.index(minprofit)
minmonth = months[indexmin]

# Create a .txt file to contain the vote analysis
write_file = os.path.join('analysis', 'financial_analysis.txt')
filewriter = open(write_file, mode = 'w')

# Print analysis to file
filewriter.write(" \n")
filewriter.write("Financial Analysis\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Months: {totalmonths}\n")
filewriter.write(f"Total: ${totalamount:,.0f}\n")
filewriter.write(f"Average Change: ${avgchange:,.2f}\n")
filewriter.write(f"Greatest Increase in Profits: {maxmonth} (${maxprofit:,.0f})\n")
filewriter.write(f"Greatest Decrease in Profits: {minmonth} (${minprofit:,.0f})\n")
filewriter.write(" \n")

# Close output file
filewriter.close()

# Display output on terminal
with open(write_file, 'r') as f:
    print(f.read())
