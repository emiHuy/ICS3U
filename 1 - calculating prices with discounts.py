while True:
  purchases=float(input("How much are your purchases? "))
  if purchases<0:
    print("Invalid.\n")
    continue
  break
if purchases<25:
  finalCost=purchases
elif purchases<50:
  finalCost=purchases-purchases*0.1
elif purchases<75:
  finalCost=purchases-purchases*0.2
elif purchases<100:
  finalCost=purchases-purchases*0.3
else:
  finalCost=purchases-purchases*0.4
print(f"The final cost to you is ${finalCost:0.2f}")