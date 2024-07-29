sum=0
while True:
  num=int(input("How many marks do you have? "))
  if num>=0:
    break
  print("invalid")
for i in range(num):
  mark=int(input(f"Enter mark {i+1}: "))
  sum+=mark
print(f"The average is: {round(sum/num,1)}")