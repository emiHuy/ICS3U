### Exercise1
def Exercise1():
  print("Exercise 1")
  # remember to indent all lines inside THIS def
  # for all your code to exercise 1

  # asks user about weather
  weather=input("What is the weather today? ")

  # output suggestions based on user input
  match weather:
    case "sunny":
      print("I would recommend you wear sunglasses!")
    case "rain":
      print("Bring an umbrella and raincoat!")
    case "snow":
      print("Bring some winter boots!")
    case "cold":
      print("Dress warmly! Wear a hat, mittens, and a jacket!")
    case "hot":
      print("Bring some cold water!")
      

def Exercise2():
  # indent all your code for exercise 2
  print("Exercise 2")

  # ask user for their role
  role=input("Are you an administrator, teacher, or student?: ")

  # output result based on role
  match role:
    case "administrator"|"teacher":    
      print("Administrators and teachers get keys!")
    case "student":
      print("Students do not get keys!")
    case _:
      print("You can only be administrator, teacher, or student!")


def Exercise3():
  # same here...
  print("Exercise 3")

  # asks user for item, cost, and amount they are buying
  item=input("What is the item? ")
  cost=float(input("How much is one item/package regularly? $"))
  amount_bought=int(input("How many are you buying? "))

  # function to calculate and output discount
  def discountout(): 
    print("Your discount rate is " + str(round(discount*100)) + "%")
    final = round(amount_bought*cost*(1-discount),2)
    print ("Your final total for " + item + " is $" + str(format(final,'.2f')))

  # matches the discount percentage to the amount of an item bought and calls the discountout function above
  match amount_bought:
    case 1:
      discount = 0
      discountout()
    case 2|3:
      discount = 0.1
      discountout()      
    case 4|5: 
      discount = 0.2
      discountout()     
    case 6:
      discount = 0.3
      discountout()     
    case _:
      print ("You may not buy MORE than 6 items.")

# This statment will run ONE of the above def's, 
# just change the number based on which def you want to run.
Exercise3()