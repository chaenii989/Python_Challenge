# Import dependencies and define source file path
import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)


pypoll_file = os.path.join('..','Resources','election_data.csv')

# Define empty Lists
votes = []
candidates = []
candidates_name = []
votes_per_candidates = []
votes_percent = []

# Open and read csv file info
with open(pypoll_file, encoding = "utf-8") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    
    # Skip header
    next(csvreader)

    # For Loop - Read through each row in csv data
    for row in csvreader:

        # Add info in Lists
        votes.append(row[0])
        candidates.append(row[2])
        
        # Count of the number of votes
        vote_count = len(votes)

    # Another for loop within Candidates List
    for name in set(candidates):

        # Get name, vote counts from each candidates and percentage
        candidates_name.append(name)
        total_votes = candidates.count(name)
        votes_per_candidates.append(total_votes)

        percent = (total_votes/vote_count)*100
        votes_percent.append(percent)

    # Get winner info
    winner_votes = max(votes_per_candidates)
    winner_name = candidates_name[votes_per_candidates.index(winner_votes)]
    
    # Print in terminal
    output = ("\nElection Results\n"
    "------------------------\n"
    f"Total Votes : {vote_count:,}\n"
    "------------------------\n")
    
    for i in range(len(candidates_name)):
        output += f"{candidates_name[i]} : {votes_percent[i]:.3f}% ({votes_per_candidates[i]:,})\n"
    output += f"------------------------\nWinner : {winner_name}\n------------------------\n"

print(output)

# Export a text file

output_file = os.path.join('..','Output','election_data.txt')

with open(output_file, "w") as text:

    text.write(output)







