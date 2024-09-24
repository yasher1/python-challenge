"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
greatest_increase=[]
greatest_decrease=[]
average_net_change=0
value=0
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row=next(reader)

    # Track the total and net change
    total_months+=1
    total_net+=int(first_row[1])
    value=int(first_row[1])
    greatest_increase.append(first_row[0])
    greatest_increase.append(first_row[1])
    greatest_decrease.append(first_row[0])
    greatest_decrease.append(first_row[1])

    # Process each row of data
    for row in reader:

        # Track the total
        total_months+=1
        total_net+=int(row[1])

        # Track the net change
        change=int(row[1])-value
        average_net_change+=change
        value=int(row[1])


        # Calculate the greatest increase in profits (month and amount)
        if int(greatest_increase[1])<change:
            greatest_increase[0]=row[0]
            greatest_increase[1]=change

        # Calculate the greatest decrease in losses (month and amount)
        if int(greatest_decrease[1])>change:
            greatest_decrease[0]=row[0]
            greatest_decrease[1]=change



# Calculate the average net change across the months


# Generate the output summary
print(total_months)
print(total_net)
print(average_net_change/(total_months-1))
print(greatest_increase)
print(greatest_decrease)
# Print the output
