# Import dependencies and define source file path
import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)


pybank_file = os.path.join('..','Resources','budget_data.csv')

# Define Empty Lists & variables
Month = []
Profit = []
Changes = []

month_counts = 0
net_profit = 0
initial_profit = 0
net_profit_changes = 0

# Open and read csv file info
with open(pybank_file, encoding ="utf-8") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    
    # Skip header
    next(csvreader)

    # For Loop - Read through each row in csv data
    for i, row in enumerate(csvreader):

        # Add info in Lists
        Month.append(row[0])
        Profit.append(row[1])
        
        # Count of months
        month_counts = month_counts + 1
        
        # Net total amount of "Profit/Losses"
        final_profit = int(row[1])
        net_profit = net_profit + final_profit

            
        # Changes in Profit/Losses
        monthly_changes = final_profit - initial_profit

        # during first month monthly change is 0
        if i == 0:
            monthly_changes = 0

        Changes.append(monthly_changes)
        net_profit_changes = net_profit_changes + monthly_changes

        initial_profit = final_profit

        # Get Average / Maximun & minimum amount

        greatest_increase = max(Changes)
        greatest_decrease = min(Changes)

        increase_date = Month[Changes.index(greatest_increase)]
        decrease_date = Month[Changes.index(greatest_decrease)]
    average_change = net_profit_changes/(month_counts-1) 

    # Print in terminal
    output = ("\nFinancial Analysis\n"
    "---------------------------\n"
    f"Total Months : {month_counts}\n"
    f"Total : ${net_profit:,}\n"
    f"Average Change : $ {average_change:,.2f}\n"
    f"Greatest Increase in Profits : {increase_date} (${greatest_increase:,})\n"
    f"Greatest Decrease in Loses : {decrease_date} (${greatest_decrease:,})\n")

    print(output)

# Export a text file

output_file = os.path.join('..','Output','budget_data.txt')

with open(output_file, "w") as text:

    text.write(output)













