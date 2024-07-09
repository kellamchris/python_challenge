#PyBank Challenge

#import modules and set path
import os

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#store content in lists
    #months = []
    #total_profit = []
greatest_increase = []
greatest_decrease = []

#read file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    row_count = 0
    net_total = 0
    previous_profit = None
    changes_profit = []

    #iterate through the rows to count the number of months
    for row in csvreader:
        row_count += 1

        profit_amount = int(row[1])         #calculate net total amount of Profit/Losses

        if previous_profit is not None:     #calculate the changes in Profit/Losses over the entire period
            change_profit = profit_amount - previous_profit
            changes_profit.append(change_profit)

        previous_profit = profit_amount 

        net_total += profit_amount

average_change = sum(changes_profit)/len(changes_profit) if changes_profit else 0   #calculate the average change



#calculate the greatest increase in profits (date and amount)



#calculate the greatest decreae in profits (date and amount)





#output the results to the terminal and a text file
print("Total Months:", row_count)

print(f"Total: {net_total}")
#print(f"Change: {change_profit}")
print(f"Average Change: {average_change}")
