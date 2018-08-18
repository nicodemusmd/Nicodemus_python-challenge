import os
import csv

poll_file = os.path.join("Resources", "election_data.csv")
output_poll = os.path.join("Resources", "poll_output.csv")

candidates = []
votes = 0
votes_tracker = []
cand_votes = 0
cand = []
candidateVotes = {}

with open(poll_file, newline = '', encoding = "UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)

    for row in csv_reader:
        votes += 1
        if str(row[2]) not in candidates:
            candidates = candidates + [str(row[2])]
            candidateVotes[str(row[2])] = 1

        else:
             candidateVotes[str(row[2])] += 1  

#print(candidates) #for reference
#print(len(candidates)) #for reference
#print(candidateVotes) #for reference

print("Election Results")
print("----------------------")
print(f'Total Votes: {votes} ')
print("----------------------")
for i in range(0,len(candidates)):
    print(f'{candidates[i]}: {round(candidateVotes[candidates[i]]/votes*100, 5)}%')
winner = max(candidateVotes, key=candidateVotes.get)
print("----------------------")
print(f'Winner: {winner}')


with open(output_poll, 'w', newline ='') as csv_file:
    csv_writer csv.writer(csv_file, delimiter = ',')
    csv_writer.writer(['Election Results'])
    csv_writer.writer(['Total Votes ', str(votes)])
    for i in range(0,len(candidates)):
        print(f'{candidates[i]}: {round(candidateVotes[candidates[i]]/votes*100, 5)}%')
    csv_writer.writer(f'{candidates[i]}: {round(candidateVotes[candidates[i]]/votes*100, 5)}%')
    csv_writer.writer(['Winner', {winner}])