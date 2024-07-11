#import modules and set path
import os

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#read file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    # Read the header row first
    csv_header = next(csvreader)

    #store variables
    row_count = 0
    net_total = 0
    previous_profit = None
    changes_profit = []
    max_increase_row = None
    max_decrease_row = None

    #iterate through the rows to count the number of months
    for row in csvreader:
        row_count += 1

        date = row[0]
        
        profit_amount = int(row[1])                                                 

        if previous_profit is not None:                                             #begin calculating the changes in Profit/Losses
            change_profit = profit_amount - previous_profit

            if max_increase_row is None or change_profit > max_increase_row[2]:     #calculate the greatest increase in profits (date and amount)
                max_increase_row = [date, profit_amount, change_profit]

            if max_decrease_row is None or change_profit < max_decrease_row[2]:     #calculate the greatest decrease in profits (date and amount)
                max_decrease_row = [date, profit_amount, change_profit]

            changes_profit.append(change_profit)                                    #final calcluation of changes over the entire period

        previous_profit = profit_amount 
        net_total += profit_amount                                                  #calculate net total amount of Profit/Losses

average_change = sum(changes_profit)/len(changes_profit) if changes_profit else 0   #calculate the average change


#output the results to the terminal
print("Financial Analysis")
print("---------------------------------")
print("Total Months:", row_count)
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change: .2f}")
print(f"Greatest Increase in Profits: {max_increase_row[0]} (${max_increase_row[2]})")
print(f"Greatest Increase in Profits: {max_decrease_row[0]} (${max_decrease_row[2]})")

#specify path to write file to
output_file = os.path.join("analysis", "analysis.txt")

#write the results to a .txt file
with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------------------\n")
    file.write(f"Total Months: {row_count}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change: .2f}\n")
    file.write(f"Greatest Increase in Profits: {max_increase_row[0]} (${max_increase_row[2]})\n")
    file.write(f"Greatest Increase in Profits: {max_decrease_row[0]} (${max_decrease_row[2]})\n")