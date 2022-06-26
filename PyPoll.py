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

# Open the election results and read the file.
# one way: election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print each row in the CSV file.
    #original: for row in file_reader:
        #print(row)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    
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