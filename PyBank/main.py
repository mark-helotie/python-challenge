# PyBank --- Python Challenge

# import modules os and csv
import os
import csv

# creating lists to store data
months = []
profitloss = []

# set path for the input file
budgetcsv = os.path.join('Resources', 'budget_data.csv')

# open the CSV
with open(budgetcsv, newline="") as csvfile:
    budgetreader = csv.reader(csvfile, delimiter=",")

    # skip the header row
    next(budgetreader)

    # loop through the CSV
    for row in budgetreader:
        # add date
        months.append(row[0])
        # add Profit/Loss
        profitloss.append(float(row[1]))

# calculate the total months
totalmonths = (len(months))

# calculate the net total amount
totalamount = sum(profitloss)

# calculate the average change per month
avgchange = totalamount / totalmonths

# calculate the greatest increase
maxprofit = max(profitloss)

# use the index of the greatest increase to find the corresponding date
indexmax = profitloss.index(maxprofit)
maxmonth = months[indexmax]

# calculate the greatest decrease 
minprofit = min(profitloss)

# use the index of the greatest decrease to find the corresponding date
indexmin = profitloss.index(minprofit)
minmonth = months[indexmin]

# format the output accordingly
financialanalysis = (f'''
Financial Analysis
----------------------------------
Total Months: {totalmonths}
Total: ${totalamount:.2f}
Average Change: {avgchange:.2f}
Greatest Increase in Profits: {maxmonth} ({maxprofit:.2f})
Greatest Decrease in Profits: {minmonth} ({minprofit:.2f})

''')

# print out the analysis in the terminal
print(financialanalysis)

# create a .txt file containing the same analysis
analysispath = os.path.join('analysis', 'financial_analysis.txt')
with open(analysispath,'w') as textfile:
    textfile.write(financialanalysis)
