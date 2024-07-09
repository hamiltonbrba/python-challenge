# python-challenge
Module 3 Challenge - PyBank &amp; PyPoll

## Description
**Bank Analysis Script (main-Bank.py)**
Overview

This Python script analyzes financial records from a dataset (budget_data.csv). The dataset contains two columns: "Date" and "Profit/Losses". The script calculates the following:

- Total number of months included in the dataset
- Net total amount of "Profit/Losses" over the entire period
- Changes in "Profit/Losses" over the entire period and the average of those changes
- Greatest increase in profits (date and amount) over the entire period
- Greatest decrease in profits (date and amount) over the entire period
- The results are printed to the terminal and exported to a text file in a designated folder.

**Usage**
1. Ensure the dataset file (budget_data.csv) is in the same directory as the script.
2. Run the script: python main-Bank.py
  
**Output**
- The results are displayed in the terminal.
- The results are saved in a text file named 'financial_analysis.txt' in the 'analysis' folder.

**Poll Analysis Script (main-Poll.py)**
Overview
This Python script helps a small, rural town modernize its vote-counting process by analyzing poll data from a dataset (election_data.csv). The dataset contains three columns: "Voter ID", "County", and "Candidate". The script calculates the following:

- Total number of votes cast
- Complete list of candidates who received votes
- Percentage of votes each candidate won
- Total number of votes each candidate won
- Winner of the election based on popular vote
- The results are printed to the terminal based on user input and exported to a text file in a designated folder.

**Usage**
1. Ensure the dataset file (election_data.csv) is in the same directory as the script.
2. Run the script: python main-Poll.py
3. When prompted, enter yes or no to choose whether to display the election results.

**Output**
- The results are displayed in the terminal if the user chooses to see them.
- The results are saved in a text file named 'election_results.txt' in the 'analysis' folder if the user opts to display the results.
