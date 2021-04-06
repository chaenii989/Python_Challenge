# Import dependencies and define source file path
import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
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
    print("Election Results")
    print("------------------------")
    print(f"Total Votes : {vote_count}")
    print("------------------------")
    
    for i in range(len(candidates_name)):
        print(f"{candidates_name[i]} : {round(votes_percent[i],2)}% ({votes_per_candidates[i]})")

    print("------------------------")
    print(f"Winner : {winner_name}")
    print("------------------------")

# Export a text file

output_file = os.path.join('..','Output','election_data.txt')

with open(output_file, "w") as text:

    text.write("Election Results"+ "\n")
    text.write("------------------------\n")
    text.write(f"Total Votes : {vote_count}" + "\n")
    text.write("------------------------\n")
    for i in range(len(candidates_name)):
        text.write(f"{candidates_name[i]} : {round(votes_percent[i],2)}% ({votes_per_candidates[i]})" + "\n")
    text.write("------------------------\n")
    text.write(f"Winner : {winner_name}" + "\n")
    text.write("------------------------\n")







