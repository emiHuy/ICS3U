bigNumList=[]
def biggestNumber(x,y,z):
  numList=[x,y,z]
  return max(numList)

def numInput(prompt):
  while True:
    try:
      variable=float(input(prompt))
    except ValueError:
      print("That is not a number, try again.")
      continue
    return variable

while True:
  num1=numInput("Enter any number: ")
  num2=numInput("Enter a second number: ")
  num3=numInput("Enter one more number: ")
  print(f"The largest number of the three is  {biggestNumber(num1,num2,num3)}")
  bigNumList.append(biggestNumber(num1,num2,num3))
  play=input("Do you want to do it again? ")
  if play in ('n','N','no','No','NO'):
    break
print(f"The largest numbers were: {bigNumList}")
print("Goodbye")