# PyPoll --- Python Challenge

# Import os and csv modules
import os
import csv

# Initialize variables
candidates = []
num_votes = 0
vote_counts = []

# Set path for the input file
input_path = os.path.join('Resources', 'election_data.csv')

# Open the CSV
with open(input_path,newline="") as csvfile:
    csvreader = csv.reader(csvfile)

    # Skip the header row
    next(csvreader,None)

    # Loop through the CSV and process each vote
    for row in csvreader:

        # Add to total number of votes
        num_votes = num_votes + 1

        # Candidate voted for
        candidate = row[2]

        # If candidate has other votes then add to their vote tally
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
            
        # Else create a new spot in the list for that candidate
        else:
            candidates.append(candidate)
            vote_counts.append(1)

percentages = []
max_votes = vote_counts[0]
max_index = 0

# Find percentage of vote for each candidate and the winner
for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/num_votes*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        max_index = count
winner = candidates[max_index]

# Create a .txt file to contain the vote analysis
write_file = os.path.join('analysis', 'pypoll_results_summary.txt')
filewriter = open(write_file, mode = 'w')

# Print analysis to file
filewriter.write("--------------------------\n")
filewriter.write("Election Results\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Votes: {num_votes:,}\n")
for count in range(len(candidates)):
    filewriter.write(f"{candidates[count]}: {percentages[count]:.3f}% ({vote_counts[count]:,})\n")
filewriter.write("---------------------------\n")
filewriter.write(f"Winner: {winner}\n")
filewriter.write("---------------------------\n")

# Close output file
filewriter.close()

# Display output on terminal
with open(write_file, 'r') as f:
    print(f.read())
