import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
os.chdir(dir_path)

pybank_file = os.path.join('..','Resources','budget_data.csv')

Months = []
Profit = []

with open(pybank_file, encoding = "utf-8") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)

    for row in csvreader:

        Months.append(row [0])
        print(len(Months))

        Profit.append(int(row [1])
        #print(sum(Profit))
