#import modules and set path
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#read file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    #Read the header row first
    csv_header = next(csvreader)

    #store variables
    total_votes = 0
    candidate_votes = {}

    #iterate through the rows
    for row in csvreader:
        
        #list the candidates who are running
        candidate = row[2]
        
        #count the number of votes
        total_votes += 1

        #calculate the number of votes for each candidate
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 1
        else:
            candidate_votes[candidate] += 1

#calculate the winner
winner = max(candidate_votes, key=candidate_votes.get)  

#output the results to the terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes:", total_votes)
print("----------------------------")

#calculate percentage of and total votes for each candidate and print results in terminal
for candidate, votes in candidate_votes.items():
    percentage = (votes/total_votes)*100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

#print the winner in the terminal
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")


#specify path to write file to
output_file = os.path.join("analysis", "analysis.txt")

#write the results to a .txt file
with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("----------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = (votes/total_votes)*100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("----------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("----------------------------")