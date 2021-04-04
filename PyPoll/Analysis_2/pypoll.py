import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
os.chdir(dir_path)

output_file = os.path.join('..','Resources','election_data.csv')



with open(output_file, encoding = "utf-8") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    for row in csvreader:
        print (row)
