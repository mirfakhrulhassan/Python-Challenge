import os
import csv

voter_id = []
county = []
candidate = []
candidate_unique = []
unique_cnt = []


flpth = os.path.join("D:\\UOFT DATA ANALYTICS\\Homeworks\\3 Python Homework\\Big Data Analysis using Python\\python-challenge\\PyPoll\\election_data.csv")

with open (flpth,newline="",encoding="UTF-8") as csvFile:
    csvReader = csv.reader(csvFile,delimiter=",")

    header  = next(csvReader)
    
    for row in csvReader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    candidateSet = set(candidate)
    candidate_unique = list(candidateSet)
    
    for x in range(len(candidate_unique)):
        unique_cnt.append(0)
    
for y in range(len(candidate_unique)):
    for r in range(len(candidate)):
        if candidate[r]==candidate_unique[y]:
            unique_cnt[y] =unique_cnt[y]+1
    
    
max = 0 

print("Election Results")
print("---------------------------------------------------------")
print(f"Total Votes: {len(voter_id)}")
print("---------------------------------------------------------")
for z in range(len(candidate_unique)):
    print(f"{candidate_unique[z]}: {(unique_cnt[z]/len(voter_id))*100}%  ({unique_cnt[z]})")
    if unique_cnt[z]>=max:
        max = unique_cnt[z]
        winner = candidate_unique[z]
    
print("---------------------------------------------------------")
print(f"Winner: {winner}")
print("---------------------------------------------------------")