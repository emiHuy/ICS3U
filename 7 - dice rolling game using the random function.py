import random
play="yes"
def playAgain():
  while True:
    askPlay=input("Do you want to play again? (yes/no) ")
    if askPlay=="yes":
      return "yes"
    elif askPlay=="no":
      return "no"
    else:
      print("Please enter yes or no")

while play=="yes":
  numRolls=0
  roll=0
  first =random.randint(1,6)
  print(f"Your first roll and point value is: {first}")
  while roll!=first:
    roll=random.randint(1,6)
    print(f"Next roll is: {roll}")
    numRolls+=1
  print(f"It took {numRolls} times to get your point again.")
  play=playAgain()
print("goodbye")