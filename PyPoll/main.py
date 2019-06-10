import os
import csv

voter_id = []
county = []
candidate = []
candidate_unique = []

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

print("Election Results")
print("---------------------------------------------------------")
print(f"Total Votes: {len(voter_id)}")
print("---------------------------------------------------------")
for x in range(len(candidate_unique)):
    print(candidate_unique[x])

print("---------------------------------------------------------")
print("Winner: ")
print("---------------------------------------------------------")