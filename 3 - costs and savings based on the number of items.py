while True:
  itemCost=float(input("What is the cost of one item? $"))
  if itemCost>=1:
    break
  print("invalid")
while True:
  numItems=int(input("How many items do you want to buy? "))
  if 1<=numItems<=100:
    break
  print("invalid")
    
match numItems:
  case 1|2:
    savings=0
  case 3|4:
    savings=0.1
  case 5|6:
    savings=0.2
  case 7|8:
    savings=0.3
  case _:
    savings=0.4
    
finalCost=itemCost*numItems*(1-savings)
print(f"After savings, your total cost will be ${finalCost:0.2f}")