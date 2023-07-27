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


    
# Printing results and exporting to a text file
# with open(file_to_output, "w") as txt_file:
    
#     election_result = (
#         f"\n\nElection Result\n"
#         f"---------------------------"
#         f"Total Votes: {total_votes}\n"
#         f"---------------------------")
#     print(election_result, end="")

#     # Save to txt file
#     txt_file.write(election_result)
#     for canidate in canidate_votes:
#         votes = canidate_votes.get(canidate)
#         percentage_vote = float(votes) / float(total_votes) * 100

#         if (votes > count_winner):
#             count_winner = votes
#             canidate_winner = canidate 

#         vote_output = f"{canidate}: {percentage_vote:.3f}% ({votes})\n"
#         print(vote_output, end="")

#         txt_file.write(vote_output)

#     winner_summary = (
#         f"-----------------------\n"
#         f"Winner: {canidate_winner}\n"
#         f"-----------------------\n")
#     print(winner_summary)

#     txt_file.write(winner_summary)



