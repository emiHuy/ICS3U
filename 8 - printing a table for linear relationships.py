def getInput(prompt):
  while True:
    try:
      variable=float(input(prompt))
    except ValueError:
      print("invalid")
      continue
    return variable

slope = getInput("What is the slope? ")
yint= getInput("What is the y-intercept? ")

if yint<0:
    print(f"For the relationship y = {slope:0.4f}x - {abs(yint):0.1f} :")
else:
    print(f"For the relationship y = {slope:0.4f}x + {yint:0.1f} :")
  
print(f"{'x':>5}{'y':>15} ")
for x in range(10):
  y=round(slope*(x+1)+yint,2)
  print(f"{x+1:5}{y:17.2f}")