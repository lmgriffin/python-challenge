

# Read in all the rows (looping through the rows)


total_profit_losses = 0
total_months = 0

sum_profit_loses = 0



# Need profit/losses in the for loop

    profit_loses = row[1]

    total_profit_losses = total_profit_losses + profit_loses

    total_months = total_months + 1

    if total_months > 1:
        change = profit_loses - last_profit_losses

    last_profit_loses = row[1]

#After loop, write out summary stuff
print('Financial Analysis')
print('--------------------')


# Print other lines
# Print out total_profit_losses
#Print out average of profit losses, which is sum_profit_losses / (total_months - 1)