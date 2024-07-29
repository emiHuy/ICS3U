while True:
  age1 = int(input("What is the age of one child? "))
  if age1<0 or age1>100:
    print("invalid")
  else:
    break
while True:
  age2 = int(input("What is the age of another child? "))
  if age2<0 or age2>100:
      print("invalid")
  else:
    break
if age1>age2:
  print("The age of the oldest child is"+str(age1+(age1-age2)))
elif age2>age1:
  print("The age of the oldest child is "+str(age2+(age2-age1)))