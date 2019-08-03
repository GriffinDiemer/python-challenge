import os
import csv

initial_length = 0
winner = 0
most_votes = 0
count = 0
votes_received = []
vote_getter= []
votes = 0
can_votes = []
candidates= []
order = 0
percent_order = 0
length= []
recount = 0

election_csv = os.path.join('election_data.csv')

with open(election_csv, newline="") as text:
    reader = csv.reader(text, delimiter =',')
    header = next(reader)


    for row in reader:
        vote_getter.append(row[2])
        votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            length.append(initial_length)
            initial_length += 1 

    for person in candidates:
        if order <= len(candidates):
            can_votes.append(0)
            can_votes[order] = vote_getter.count(person)
            order += 1


    for x in can_votes:
        if percent_order <= len(can_votes):
            votes_received.append(0)
            votes_received[percent_order] = '%.3f'%(float((int(can_votes[percent_order])/votes)*100))
            percent_order += 1
            
    for number in can_votes:
        if most_votes <= number:
            most_votes = number
            winner = count   
        count = count + 1



with open("results.txt", 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Election Results"])

    csvwriter.writerow(["--------------------------------"])

    csvwriter.writerow([f'Total Votes: {votes}'])

    csvwriter.writerow(["--------------------------------"])


    for i in length:
        if recount <= int(i):
            csvwriter.writerow([f"{candidates[i]}: {votes_received[i]}% ({can_votes[i]})"])
    csvwriter.writerow(["--------------------------------"])

    csvwriter.writerow([f"Winner: {candidates[winner]}"])

    csvwriter.writerow(["--------------------------------"])


#if count is less than or equal to number then keep looping. if not end. in the if loop it will be (f"{candidate[count]}: {votes_received[count]}% ({can_votes[count]})

#after if statement ends print (f"Winner: {candidates[winner]})


result = open("results.txt","r")

print(result.read())
