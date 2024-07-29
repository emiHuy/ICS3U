def sortList():
  nameList.sort()

def search():
  while True:
    x=0
    search=input("What name would you like to search for? ")
    if search=='STOP':
      break
    for i in range(len(nameList)):
      if search==nameList[i]:
        print(f"{search} was found at position {i+1} in the list")
        x=1
    if x==0:
      print(f"{search} was not found in the list.")
          
print("Type the word STOP to quit entering names.")
nameList=[]
while True:
  name=input("What is the last name? ")
  if name=="STOP":
    break
  nameList.append(name)
sortList()
search()