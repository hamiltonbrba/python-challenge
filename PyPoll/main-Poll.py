# import modules
import os
import csv
import statistics

# Path to the election CSV file, output folder for election results text file
csv_file_path = os.path.join('Resources', 'election_data.csv')
output_folder = 'analysis'
output_file_path = os.path.join(output_folder, 'election_analysis.txt')

# Initialize variables - keep track of total number of votes
total_votes = 0
candidates = set()
votes_per_candidate = {}

# Read the csv file
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) # Skip the header row

    for row in csv_reader:
        total_votes += 1
        candidate = row[2]

        # Add candidate to the set of candidates
        candidates.add(candidate)

        # Total number of votes each candidate won
        if candidate in votes_per_candidate:
            votes_per_candidate[candidate] += 1
        else:
            votes_per_candidate[candidate] = 1


# Percentage of votes each candidate won
percent_votes_per_candidate = {candidate: (votes / total_votes) * 100 for candidate, votes in votes_per_candidate.items()}

# Winner of the election based on popular vote
winner = max(votes_per_candidate, key=votes_per_candidate.get)

# Create the results string
results = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)
for candidate, votes in votes_per_candidate.items():
    results += f"{candidate}: {percent_votes_per_candidate[candidate]:.3f}% ({votes})\n"
results += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print Results
print(results)

# Export results to text file
with open(output_file_path, 'w') as file:
    file.write(results)


