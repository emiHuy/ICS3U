import random

integerList=[]    
minimum=int(input("What is the lower bound? "))
maximum=int(input("What is the higher bound? "))

while True:
  integerList.append(random.randint(10,30))
  again=input("Number was added, do you want to add another? ")
  if again=="No":
    break
    
print(f"The numbers generated were: {integerList}")
integerList.sort()
print(f"Ascending order: {integerList}")
integerList.sort(reverse=True)
print(f"Descending order: {integerList}")