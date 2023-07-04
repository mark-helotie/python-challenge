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

# Format the output accordingly
financialanalysis = (f'''
Financial Analysis
----------------------------------
Total Months: {totalmonths}
Total: ${totalamount:,.0f}
Average Change: ${avgchange:,.2f}
Greatest Increase in Profits: {maxmonth} (${maxprofit:,.0f})
Greatest Decrease in Profits: {minmonth} (${minprofit:,.0f})

''')

# Print out the analysis in the terminal
print(financialanalysis)

# Create a .txt file containing the same analysis
analysispath = os.path.join('analysis', 'financial_analysis.txt')
with open(analysispath,'w') as textfile:
    textfile.write(financialanalysis)
