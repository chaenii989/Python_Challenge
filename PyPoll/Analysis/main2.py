# Import dependencies and define source file path
import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

pypoll_file = os.path.join('..','Resources','election_data.csv')

# Define empty Lists
votes = 0
candidates = []
candidates_votes = {}
winner = ['',0]

# Open and read csv file info
with open(pypoll_file, encoding = "utf-8") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    
    # Skip header
    next(csvreader)

    # For Loop - Read through each row in csv data
    for row in csvreader:

        name = row[2]

        if name not in candidates:
            candidates.append(name)
            candidates_votes[name] = 0
        
        votes += 1
        candidates_votes[name] += 1

        if candidates_votes[name] > winner[1]:
            winner[0] = name
            winner[1] = candidates_votes[name]
    
    # Print in terminal
    output = ("\nElection Results\n"
    "------------------------\n"
    f"Total Votes : {votes:,}\n"
    "------------------------\n")
    
    for name in candidates:
        output += f"{name} : {candidates_votes[name]/votes*100:.3f}% ({candidates_votes[name]:,})\n"
    output += f"------------------------\nWinner : {winner[0]}\n------------------------\n"

output_file = os.path.join('..','Output','election_data.txt')
text = open(output_file, "w")
text.write(output)
print(output)