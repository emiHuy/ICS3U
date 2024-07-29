num=10
def voting():
  tot=0
  while True:
    print("The presidential candidates are:")
    for i in range(num):
      print(f"{i+1}. {candidates[i][0]}")
    print("Type 0 to quit")
    vote=getInteger("Vote? ")
    if vote==0:
      return tot
    candidates[vote-1][1]+=1
    tot+=1

def getInteger(prompt):
  while True:
    try:
      variable=int(input(prompt))
      if 0<=variable<=num:
        return variable
      else:
        print("not negative or too big")
    except ValueError:
      print("not a number")
  
num=getInteger("How many candidates are there in the election? ")
candidates=[]
candidateVote=0
for i in range(num):
  candidate=input(f"What is candidate #{i+1}'s name? ")
  candidates.append([candidate, 0])
totalVotes=voting()
print(f"The total number of votes is: {totalVotes}")
results=[]
for i in range(num):
  results.append(candidates[i][1])
for i in range(num):
  if results[i]==max(results):
    winner=candidates[i][0]
    numVotes=candidates[i][1]
print(f"{winner} is the winner with {numVotes/totalVotes*100:.1f}% of the votes.")