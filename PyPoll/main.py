"""PyPoll Homework Starter File."""

# Import necessary modules
import os
import csv

# Files to load and output (update with correct file paths)
file_to_load=os.path.join("Resources", "election_data.csv")

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_list=[]
candidate_count=[]

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        #print(". ", end="")

        # Increment the total vote count for each row
        total_votes+=1


        # Get the candidate's name from the row
        c_name=row[2]


        # If the candidate is not already in the candidate list, add them
        if c_name not in candidate_list:
            candidate_list.append(c_name)
            candidate_count.append(0)

        # Add a vote to the candidate's count
        c_index=candidate_list.index(c_name)
        candidate_count[c_index]=candidate_count[c_index]+1
max_count=max(candidate_count)
w_index=candidate_count.index(max_count)
winner=candidate_list[w_index]

print("Election Results")
print("------------------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------------------")
print(f"{candidate_list[0]}:{round((candidate_count[0]/total_votes*100),3)}% ({candidate_count[0]})")
print(f"{candidate_list[1]}:{round((candidate_count[1]/total_votes*100),3)}% ({candidate_count[1]})")
print(f"{candidate_list[2]}:{round((candidate_count[2]/total_votes*100),3)}% ({candidate_count[2]})")
print("------------------------------------")
print(f"Winner:{winner}")
print("------------------------------------")