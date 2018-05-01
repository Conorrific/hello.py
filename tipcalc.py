print("Hello World")

subtotal = float(input("Enter the total of the bill after tax: "))
tip = float(input("Enter the percentage you would like to tip: "))
tip_percent = round((tip / 100) * subtotal, 2)
newtotal = round(tip_percent + subtotal, 2)
print(f"The subtoal of the bill is ${subtotal}, the tip amount is ${tip_percent}, the total amount due is ${newtotal}")