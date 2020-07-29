import os
import csv

#create new lists and counters
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

    #find total votes   
    for row in csv_reader:
        vote_count += 1   
        candidates = (row[2])
        #create unique group of candidates along with their total votes
        if candidates not in candidates_list:
            candidates_list.append(candidates)
            candidate_votes[candidates] = 0
        candidate_votes[candidates] = candidate_votes[candidates] + 1
#find the candidate with the most votes
potential_candidate = candidates_list[0]
winning_votes = candidate_votes[potential_candidate]

#top half of print statement
print("Election Results")
print("--------------------------------------")
print(f"Total Votes: {vote_count}")
print("--------------------------------------")

#using key to print candidates along with thier percent votes and total votes
for key in candidate_votes:
    print(f"{key}: {round(100 * candidate_votes[key]/vote_count, 2)}% ({candidate_votes[key]})")
    if candidate_votes[key] > winning_votes:
        potential_candidate = key
        winning_votes = candidate_votes[key]

print(f"Winner: {potential_candidate} with {winning_votes} votes!")        

#create output file and what to write on it
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