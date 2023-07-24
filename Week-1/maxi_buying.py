price = int(input())
including_tax = round(price * 1.08)
if including_tax < 206:
    print("Yay!")
elif including_tax == 206:
    print("so-so")
else:
    print(":(")