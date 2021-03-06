#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who receive votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
# one way: file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Initialize candidate options
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
# one way: election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    #Print each row in the CSV file.
    #original: for row in file_reader:
        #print(row)
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate, add the candidate name.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
            
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
    
        # Save the final vote count to the text file.
        txt_file.write(election_results)

        # Determine the percentage of votes for each candidate by looping through the counts.
        # Iterate through the candidate list.
        for candidate_name in candidate_votes:
            # Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
            # Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (
                f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Print out each candidate's name, vote count, and percentage of
            # votes to the terminal.
            #comment out: print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)

            # Save the candidate results to our text file.
            txt_file.write(candidate_results)

            # Determine winning vote count and candidate
            # Determine if the votes is greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percent =
                # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name

        # Print out the winning candidate, vote count and percentage to
        # terminal.
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
            #comment out: print(winning_candidate_summary)
        print(winning_candidate_summary)
        # Save the winning candidate's results to the text file.
        txt_file.write(winning_candidate_summary)
        
        # Print the candidate name and percentage of votes 
        # Skill Drill by adding ":.1f" before the % it formatted to one decimal place
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

    # Print the total votes.
    #print(total_votes)

    # Print the candidate list.
    #print(candidate_options)

    # Print the candidate vote dictionary.
    #print(candidate_votes)

        
        # To do: perform analysis.
        #print(election_data)

    # Close the file.
    #election_data.close()

    # Create a filename variable to a direct or indirect path to the file.
    #file_to_save = os.path.join("analysis", "election_analysis.txt")

    # Use the open statement to open the file as a text file..
    # outfile = open(file_to_save, "w")

    # Using the with statement open the file as a text file.
    #with open(file_to_save, "w") as txt_file:

        # Write some data to the file.
        #outfile.write("Hello World")

        # Write three counties to the file.
        # First method:
        #txt_file.write("Arapahoe, ")
        #txt_file.write("Denver, ")
        #txt_file.write("Jefferson")
        # Second method:
        #txt_file.write("Arapahoe, Denver, Jefferson")
        # Newline escape sequence
        #txt_file.write("Arapahoe\nDenver\nJefferson")

        # Skill Drill
        #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

        # CLose the file
        #outfile.close()

    # Using the open() function with the "w" mode we will write data to the file.
    # open(file_to_save, "w")