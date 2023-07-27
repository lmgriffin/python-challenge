import os
import csv

csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

# Vote Counter
total_votes = 0


canidate_choices = []
canidate_votes = {}

#Counts for who won
canidate_winner = ""
count_winner = 0


with open(csvpath) as election_data:
    csvreader = csv.reader(election_data)

    csv_header = next(csvreader)

    #Loop
    for row in csvreader:

        #Total votes cast
        total_votes = total_votes + 1

        # Getting name from each row
        canidate_name = row[2]

        if canidate_name not in canidate_votes:
            canidate_choices.append(canidate_name)

            canidate_votes[canidate_name] = 0
        
        canidate_votes[canidate_name] = canidate_votes[canidate_name] + 1

    print("-----------------------")
    print("Election Results")
    print("-----------------------")

    for canidate in canidate_votes:
        votes = canidate_votes.get(canidate)
        percentage_vote = float(votes) / float(total_votes) * 100

        if (votes > count_winner):
            count_winner = votes
            canidate_winner = canidate 

        vote_output = f"{canidate}: {percentage_vote:.3f}% ({votes})\n"
        print(vote_output, end="")

    print("-----------------------")
    print("Winner: " + canidate_winner)
    print("-----------------------")

with open('Analysis.txt', 'w') as text:

    text.write("------------------------------\n")
    text.write(" Election Results")
    text.write("------------------------------\n")
    text.write("Winner: " + str(canidate_winner))
    
