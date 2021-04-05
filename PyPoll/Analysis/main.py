# Import dependencies and define source file path
import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
os.chdir(dir_path)


pypoll_file = os.path.join('..','Resources','election_data.csv')

Candidates = []
Votes_Count_Candidates = []

vote_count = 0

with open(pypoll_file, encoding = "utf-8") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)

    for row in csvreader:

        vote_count = vote_count + 1
        Candidates.append(row[2])








