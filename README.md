# Election_Analysis

## Overview of Election Audit
A Colorado Board of Elections employee has provided the following task to complete the election audit of a recent local congressinal election:

1. Determine the total number of votes cast, candidates who receive votes with percentages and total number of votes each candidate won and the winner of the election based on popular vote.
2. Determine voter turnout for each county, percentages of votes from each county out of the total count and the county with the highest turnout. 

## Resources
- Data Source: election_results.csv
- Software: Python 3.10, Visual Studio Code 1.68.1

## Election-Audit Results
- How many votes were cast in this congressional election?
  - There were 369,711 votes cast in the election.
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct
  - The scripted code below generated the following analysis:
      
  ![County_Votes](https://user-images.githubusercontent.com/106962921/175839045-b0717420-6f6d-4186-a08d-afc642f95a2c.png)

        # 6a: Write a for loop to get the county from the county dictionary.
        for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        votes = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
                f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
         # 6d: Print the county results to the terminal.
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > county_turnout_count) and (vote_percentage > county_turnout_percentage):
            county_turnout_count = votes
            county_turnout_percentage = vote_percentage
            county_turnout = county_name
- Which county had the largest number of votes?
  - The county with the largest number of votes was Denver which was determine using the code seen below:
        
        # 7: Print the county with the largest turnout to the terminal.
        county_turnout_summary = (
            f"-------------------------\n"
            f"Largest County Turnout: {county_turnout}\n"
            f"-------------------------\n")
        # 8: Save the county with the largest turnout to a text file.
        txt_file.write(county_turnout_summary)
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  - The scripted code below generated the following analysis:
  
   ![Candidate_Votes](https://user-images.githubusercontent.com/106962921/175839324-e22cb6e7-acb1-45ab-a405-6e821a5fe502.png)

        # Save the final candidate vote count to the text file.
        for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  - The winner of the election was Diana DeGette who received 73.8% of the vote and 272,892 number of votes  

## Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
