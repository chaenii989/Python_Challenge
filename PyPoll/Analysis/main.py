# Import dependencies and define source file path
import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
os.chdir(dir_path)


pypoll_file = os.path.join('..','Resources','election_data.csv')

votes = []
candidates = []
candidates_name = []
votes_per_candidates = []
votes_percent = []

with open(pypoll_file, encoding = "utf-8") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)

    for row in csvreader:

        votes.append(row[0])
        candidates.append(row[2])
        
        vote_count = len(votes)

    for name in set(candidates):

        candidates_name.append(name)
        
        total_votes = candidates.count(name)
        votes_per_candidates.append(total_votes)
        
        percent = (total_votes/vote_count)*100
        votes_percent.append(percent)

    winner_votes = max(votes_per_candidates)
    winner_name = candidates_name[votes_per_candidates.index(winner_votes)]
    
    print("Election Results")
    print("------------------------")
    print(f"Total Votes : {vote_count}")
    print("------------------------")
    
    for i in range(len(candidates_name)):
        print(f"{candidates_name[i]} : {round(votes_percent[i],3)}% ({votes_per_candidates[i]})")

    print("------------------------")
    print(f"Winner : {winner_name}")
    print("------------------------")








