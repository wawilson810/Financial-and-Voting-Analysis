import os
import csv

#Writing the paths for reading in the csv file as well as writing the txt file with the results respectively
path = "C:\\Users\\wawil\\python-challenge\\PyPoll\\"
writepath = path + "analysis\\results.txt"
poll_csv = os.path.join(path, 'Resources','election_data.csv')

#A simple function to display a line of dashes to be used when displaying the results
def line():
    print("--------------------")

#Opening the csv file to read in the data
with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Initializing a list of for the unique candidates, the total votes as 0 and a dictionary with the candidate as the key and the votes they received as the value
    candidates = []
    total = 0
    votes = {}
    
    #Storing the header row and moving past it to get to the data
    csv_header = next(csvreader)

    #Reading through the data row by row
    for row in csvreader:

        #Testing if the candidate in each row is already in the list of candidates. If they are not, they are added to the list.
        #Additionally, they are added to the dictionary as a key with the initial value of 1 vote.
        #If the candidate is already on the list, a vote is added to their total
        if row[2] not in candidates:
            candidates.append(row[2])
            votes[row[2]] = 1
        else:
            votes[row[2]] += 1
        #Counting the total votes
        total+=1
    
    #Displaying the results of the election in the terminal
    print("Election Results")
    line()
    print(f"Total Votes: {total}")
    line()

    #Looping through the candidates and displaying them, the percentage of the vote they received as well as the total votes they received
    for keys in votes:
        print(f"{keys}: {round( 100*(votes[keys]/total),3)}% ({votes[keys]})")
        #Testing if each candidate received the maximum number of votes to determine the winner
        if votes[keys] == max(votes.values()):
            winner = keys
    
    line()
    print(f"Winner: {winner}")
    line()

#Exporting what was displayed in the terminal to a txt file in the analysis folder
with open(writepath, "w") as file:
    file.write('\n'.join(["Election Results", "--------------------------", 
    f"Total Votes: {total}"]))
    for keys in votes:
        file.writelines(['\n', '\n'.join([f"{keys}: {round( 100*(votes[keys]/total),3)}% ({votes[keys]})"])])
    file.writelines(['\n','\n'.join([f"Winner: {winner}", "--------------------------"])])
