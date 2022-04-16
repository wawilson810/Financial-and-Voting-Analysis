import os
import csv

path = "C:\\Users\\wawil\\python-challenge\\PyPoll\\"
writepath = path + "analysis\\results.txt"
poll_csv = os.path.join(path, 'Resources','election_data.csv')

def line():
    print("--------------------")

with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    candidates = []
    total = 0
    votes = {}
    csv_header = next(csvreader)
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
            votes[row[2]] = 1
        else:
            votes[row[2]] += 1
        total+=1
    
    print("Election Results")
    line()
    print(f"Total Votes: {total}")
    line()

    for keys in votes:
        print(f"{keys}: {round( 100*(votes[keys]/total),3)}% ({votes[keys]})")
        if votes[keys] == max(votes.values()):
            winner = keys
    
    line()
    print(f"Winner: {winner}")
    line()

with open(writepath, "w") as file:
    file.write('\n'.join(["Election Results", "--------------------------", 
    f"Total Votes: {total}"]))
    for keys in votes:
        file.writelines(['\n', '\n'.join([f"{keys}: {round( 100*(votes[keys]/total),3)}% ({votes[keys]})"])])
    file.writelines(['\n','\n'.join([f"Winner: {winner}", "--------------------------"])])
