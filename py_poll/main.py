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
candidate_list = []
candidate_count = []
num_of_votes = []
pct_of_votes = []

# Initialize variables
total_votes = 0

# Tasks:
# 1. Total number of votes                      total_votes = total_votes + 1
# 2. List of candidates                         candidates.append(row[2])
# 3. Percent of votes for each candidate        (candidate_list/total_votes)*100
# 4. Number of votes for each candidate         candidate_list = candidate_list + 1
# 5. Winner                                     max(candidate_list)

# Open and read csv
with open(input_path, 'r', encoding='utf8') as polling_file:
    polling_reader = csv.reader(polling_file, delimiter=',')

    # Read the header row first
    polling_header = next(polling_reader)

    # Read therough each row of data after the header
    for row in polling_reader:

        # Calculate total number of votes cast
        total_votes = total_votes + 1

        # Add each candidate name to the list of candidates
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            
        num_of_votes.append(row[2])

    # Loop through each candidate and add the number of votes for each
    for candidate in candidate_list:
        candidate_count.append(num_of_votes.count(candidate))
        pct_of_votes.append(round(num_of_votes.count(candidate)/total_votes*100,3))
    
    # Find the winner
    winner = max(candidate_list)
 
    # Print the results
    print('Election Resuls')
    print('-------------------------')
    print(f'Total Votes: {total_votes}')
    print('-------------------------')
    for i in range(len(candidate_list)):
        print(f'{candidate_list[i]}: {pct_of_votes[i]}% ({candidate_count[i]})')
    print('-------------------------')
    print(f'Winner: {winner}')
    print('-------------------------')

with open(output_path, "w") as txt_file:
    txt_file.write('Election Resuls')
    txt_file.write('\n-------------------------')
    txt_file.write(f'\nTotal Votes: {total_votes}')
    txt_file.write('\n-------------------------')
    for i in range(len(candidate_list)):
        txt_file.write(f'{candidate_list[i]}: {pct_of_votes[i]}% ({candidate_count[i]})')
    txt_file.write('\n-------------------------')
    txt_file.write(f'\Winner: {winner}')
    txt_file.write('\n-------------------------')