import os
import csv
csvpath = os.path.join("Resources", "election_data.csv")

#Variables
candidates = []
votes_count = []
votes_percentage = []
total_votes = 0

#Read CSV File
with open(csvpath, newline="") as csvfile:
#Set data
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
#Creat loop
    for row in csvreader:
        # Calculate the total number of votes 
        total_votes += 1
#list of candidates who received votes - if the candidate is in the list, a vote will be counted for them
#If they are not on the list, their name will be added and the vote
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            votes_count.append(1)
        else:
            index = candidates.index(row[2])
            votes_count[index] += 1

 # The percentage of votes each candidate won
    for votes in votes_count:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        votes_percentage.append(percentage)

 #The winner of the election based on popular vote.
    winner = max(votes_count)
    index = votes_count.index(winner)
    winner_candidate = candidates[index]


print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(votes_percentage[i])} ({str(votes_count[i])})")
print("--------------------------")
print(f"Winner: {winner_candidate}")
print("--------------------------")

#Export results to text file
output = os.path.join("Analysis", "PyPoll_results.txt")
with open(output, "w") as txtfile:
        txtfile.write("Election Results\n")
        txtfile.write("------------------------------------\n")
        txtfile.write(f"Total Votes: {total_votes}\n")
        txtfile.write("------------------------------------\n")
        for i in range(len(candidates)):
            txtfile.write(f"{candidates[i]}: {votes_percentage[i]}% {votes_count[i]}\n")
        txtfile.write("------------------------------------\n")
        txtfile.write(f"Winner: {winner}\n")
        txtfile.write("------------------------------------\n")