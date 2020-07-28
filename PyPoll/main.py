#pybank

import os

# current_working_directory = os.getcwd()
# print(current_working_directory)

# Module for reading CSV files
import csv

vote_count = 0
candidates_list = []
total_votes = []
candidate_votes = {}
percent_vote = []
percent = 0 

#define file path to open
csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

# CSV reader specifies delimiter and variable that holds contents
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader)
    # print(f"CSV Header: {csv_header}")
   
    for row in csv_reader:
        vote_count += 1   
        candidates = (row[2])
        if candidates not in candidates_list:
            candidates_list.append(candidates)
            candidate_votes[candidates] = 0
        candidate_votes[candidates] = candidate_votes[candidates] + 1

potential_candidate = candidates_list[0]
winning_votes = candidate_votes[potential_candidate]

print("Election Results")
print("--------------------------------------")
print(f"Total Votes: {vote_count}")
print("--------------------------------------")

for key in candidate_votes:
    print(f"{key}: {round(100 * candidate_votes[key]/vote_count, 2)}% ({candidate_votes[key]})")
    if candidate_votes[key] > winning_votes:
        potential_candidate = key
        winning_votes = candidate_votes[key]

print(f"Winner: {potential_candidate} with {winning_votes} votes!")        

output_file = os.path.join("..", "PyPoll", "Analysis", "PyPoll_Analysis.text")
with open(output_file, 'w') as txtfile:

    txtfile.write("Election Results\n")
    txtfile.write("----------------------------------------------------------\n")
    txtfile.write(f"Total_Votes: {vote_count}\n")
    txtfile.write("----------------------------------------------------------\n")
    for key in candidate_votes:
        txtfile.write(f"{key}: {round(100 * candidate_votes[key]/vote_count, 2)}% ({candidate_votes[key]}) \n")
    txtfile.write("----------------------------------------------------------\n")
    txtfile.write(f"Winner: {potential_candidate} with {winning_votes} votes!\n")
    txtfile.write("----------------------------------------------------------\n")