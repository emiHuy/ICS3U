intList=[]
def getInteger():
  while True:
    try:
      integer=int(input("Value? "))
      if integer==-1:
        break
      if integer<-1:
        print("Positive please, try again.")
    except ValueError:
      print("Integer please, try again")
    intList.append(integer)

def histogram(aList):
  print("Histogram: ")
  for value in intList:
    print("*"*value)
  
print("Enter positive integers for a list, type in -1 to stop.")
getInteger()
if len(intList)>=1:
  histogram(intList)
else:
  print("list is empty")