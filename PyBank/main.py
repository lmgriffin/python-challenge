import os
import csv

cvspath = os.path.join("PyBank", "Resources", "budget_data.csv")

# Read in all the rows (looping through the rows)

greatest_profit = 0
greatest_profit_month = ""
least_profit = 999999
least_profit_month = ""

total_profit_losses = 0
total_months = 0

sum_profit_losses = 0


# Need profit/losses in the for loop
with open(cvspath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:

        #Calculate total months here:
        total_months = total_months + 1

        #Calculate the total amount of "Profit/Losses"
        profit_losses = int(row[1])

        total_profit_losses = total_profit_losses + int(row[1])

        #Changes in "Profit/Losses" over the entire period (get total of changes)
        if total_months > 1:
            change = profit_losses - last_profit_losses
            sum_profit_losses = sum_profit_losses + change
            if change > greatest_profit:
                greatest_profit = change
                greatest_profit_month = row[0]
            if change < least_profit:
                least_profit = change
                least_profit_month = row[0]                                  
        last_profit_losses = int(row[1])

        


#After loop, write out summary stuff
print('Financial Analysis')
print('--------------------')
print("Total Months: " + str(total_months))
print("Total: " + "$" + str(total_profit_losses))
print("Average Change: " + "$" + str(int(sum_profit_losses / (total_months - 1))))
print("Greatest Increase in Profits: " + )

# Print other lines
# Print out total_profit_losses
#Print out average of profit losses, which is sum_profit_losses / (total_months - 1)