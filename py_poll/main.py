# Import modules
import os
import csv

# Paths to collect and write data
input_path = os.path.join('resources','election_data.csv')
output_path = os.path.join('resources', 'poll_analysis.txt')

# Rows
# 0 = Voter ID
# 1 = County
# 2 = Candidate

# Create 
candidates = []
num_votes = []
pct_of_votes = []

# Initialize variables
total_votes = 0

# Tasks:
# 1. Total number of votes                      total_votes = total_votes + 1
# 2. List of candidates                         candidates.append(row[2])
# 3. Percent of votes for each candidate        (candidate_list/total_votes)*100
# 4. Number of votes for each candidate         candidate_list = candidate_list + 1
# 5. Winner                                     max(candidate_list)

# One and read csv
with open(input_path, 'r', encoding='utf8') as polling_file:
    polling_reader = csv.reader(polling_file, delimiter=',')

    # Read the header row first
    polling_header = next(polling_reader)

    # Read therough each row of data after the header
    for row in polling_reader:

        # Add candidate names to the list of candidates
        candidate = row[2]
        candidates = 

        # Spoiler, find the winner
        winner = max(set(candidates), key=candidates.count)

        # Calculate total number of votes cast
        total_votes = candidates.count(winner)

        print(f'The winner is {winner} with {total_votes} votes')

        # Calculate percent of votes for each candidate
        # pct_votes = round(int(candidates/total_votes), 2)
        # pct_of_votes.append(pct_votes)

        # Calculate the number of votes for each candidate
        # num_of_votes = candidates + candidates + 1

        # Find the winner












