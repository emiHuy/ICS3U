sum=0 
def getInteger():
  while True:
    try:
      integer=int(input("Enter a positive integer in between 10 and 999999: "))
      if 10<=integer<=999999:
        break
      print("out of range")
    except ValueError:
      print("not an integer")
  return integer

positiveNum=str(getInteger())
digitList=list(positiveNum)
for digit in digitList:
  sum+=int(digit)
print(f"{positiveNum} has {len(digitList)} digits and the sum of these digits is {sum}.")