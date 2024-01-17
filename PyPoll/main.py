import os  
import csv

# File Path
election = os.path.join("python-challenge", "PyPoll", "resources", "election_data.csv")

# Initialize Variables
total_votes = 0
election_winner = []
candidate_list = []
candidate_names = {}


# Read File & Set Delimiter
with open(election) as csvfile:
    election_data = csv.reader(csvfile, delimiter= ",")

     # how to get it to read Header? "next(csv_reader)"
    header = next(csvfile)

    # Run through
    for rows in election_data:

        # The total number of votes cast
        total_votes = total_votes + 1
        
        # A complete list of candidates who received votes w/ dictionary
        candidate = rows[2]
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_names[candidate] = 0
        candidate_names[candidate] += 1
        





print("Election Results")
print("---------------------------------")
print(f"Total Votes  {total_votes}")
for candidates in candidate_list:
    print(f"{candidates}: {round(candidate_names[candidates] / total_votes * 100, 3)}% ({candidate_names[candidates]})")

print("----------------------------------")
print(f"Winner:  {max(candidate_names, key=candidate_names.get)}")
print("----------------------------------")


# Export to text file
output_path = os.path.join("python-challenge", "PyPoll", "analysis", "newelection.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    txtfile.write("Election Results\n")
    txtfile.write("---------------------------------\n")
    txtfile.write(f"Total Votes  {total_votes}\n")
    for candidates in candidate_list:
            txtfile.write(f"{candidates}: {round(candidate_names[candidates] / total_votes * 100, 3)}% ({candidate_names[candidates]})\n")

    txtfile.write("----------------------------------\n")
    txtfile.write(f"Winner:  {max(candidate_names, key=candidate_names.get)}\n")
    txtfile.write("----------------------------------\n")