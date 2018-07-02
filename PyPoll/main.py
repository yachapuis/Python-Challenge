# PyPoll
# main.py
# by Yves-Andre Chapuis
#
# ------------------------------------------
#  Require Dependencies
# ------------------------------------------
# Modules
import os
import csv  

# ------------------------------------------
#  Input File
# ------------------------------------------
# Set path for input file
csv_path = os.path.join("election_data.csv")

# ------------------------------------------
#  Output File
# ------------------------------------------
# Set path for output file
txt_output = os.path.join("election_analysis.txt") 

# ------------------------------------------
# Main
# ------------------------------------------

# Initiate variable for total number of voters
total_votes = 0

# Initiate list of candidates who received votes
candidates_list = []

# Initiate dictionary of candidates with number and percentage of votes as list
candidates_dict = {}

# Initiate variable for highest number of votes of elected candidate
highest_votes = 0

# Initiate elected candidate variable
candidate_winner = ""

# Read the csv file and converts it into lists
with open(csv_path) as election_data:
    csv_reader = csv.reader(election_data)

    # Skip first row
    next(csv_reader) 

    # Read each row of the csv_reader file in a loop
    for row in csv_reader:

        # Count the total of votes from the election
        total_votes = total_votes + 1

        # Record name of each candidate that collected at least one vote
        candidate = row[2]

        # Add every voted candidate to a list
        if candidate not in candidates_list:
            candidates_list.append(candidate)

            # Initiate value of votes for each new candidate
            candidates_dict[candidate] = 1

        # Count the total of votes by candidates
        candidates_dict[candidate] = candidates_dict[candidate] + 1

# Print the results and export the data to our text file
with open(txt_output, "w") as txt_file:

    # Print the final vote count (to terminal)
    vote_results = (
        f"\n\n-------------------------\n"
        f"ELECTION RESULTS:\n"
        f"-------------------------\n"
        f"Number of Votes: {total_votes}\n"
        f"-------------------------\n")
    print(vote_results, end="")

    # Save the final vote count to the text file
    txt_file.write(vote_results)

   # Affect total voles and percentage to each candidate in dictionary
    for candidate in candidates_dict:

        # Collect total of votes per candidate from dictionary
        candidate_votes = candidates_dict.get(candidate)
        
        # Collect vote percentage per candidate from dictionary
        candidate_percentage = (float(candidate_votes) / float(total_votes)) * 100

        # Nominate the elected candidate
        if (candidate_votes > highest_votes):
            elected_candidate = candidate
            highest_votes = candidate_votes

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {candidate_percentage:.3f}% ({candidate_votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate (to terminal)
    election_results = (
        f"-------------------------\n"
        f"Elected Candidate: {elected_candidate}\n"
        f"-------------------------\n")
    print(election_results)

    # Save the final vote count to the text file
    txt_file.write(election_results)