import os
import csv

# Create path into csv file
csvpath = os.path.join("..","Resources", "election_data.csv")

# Create variable for calculation 
total_votes = 0
candidate_percent = 0
winner_votes = 0

# Set variable value using list method 
candidates = []
vote_count = []

# Open CSV election_data file 
with open(csvpath, 'r', newline='') as csvpypoll:
    csvreader = csv.reader(csvpypoll, delimiter=',')

    # skip headers
    csv_header = next(csvreader)

    # loop through the record file election data
    for row in csvreader:
        total_votes += 1
    
    # print(total_votes)

        # Create an append for candicates
        if(row[2] not in candidates):
            candidates.append(row[2])
            vote_count.append(0)

        # Create new index for candidates
        candidateIndex = candidates.index(row[2])

        vote_count[candidateIndex] += 1

    print(f'\nElection Results\n-------------------')
    print(f'Total votes: {total_votes}')

    # loop through candidates to calculate the percentage of votes for each candicate  
    for x in range(len(candidates)):
        candidate_percent = round((vote_count[x]/total_votes)*100,3)

        # print out the candidate with percent votes count
        print(f"{candidates[x]}: {candidate_percent}% ({vote_count[x]})")

        # find winner with highest votes
        if (winner_votes < vote_count[x]):
            winner_votes = vote_count[x]
            winner = candidates[x]

    print("-----------------------------")
    print(f"Winner: {winner}")
    print("-----------------------------")        


     # name white file
    output_file = csvpath[0:-4]
    write_csvpath = f"{output_file}_pypoll_results.text"

    # open write file
    filewriter = open(write_csvpath, mode = 'w')

    # print to writer file
    filewriter.write(f"Election Results\n")
    filewriter.write("--------------------------------------------\n")
    filewriter.write(f"Total votes: {total_votes} \n")
    for x in range(len(candidates)):
        candidate_percent = round((vote_count[x]/total_votes)*100,3)
        filewriter.write("\n" + str(candidates[x]) +" : " + str(candidate_percent) + "% ("+ str(vote_count[x]) + ")\n")
    filewriter.write("----------------------------\n")
    filewriter.write(f"Winner: {winner}\n ")    
    filewriter.write("---------------------------")


    filewriter.close()
