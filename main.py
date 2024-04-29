z = input("Provide an integer number: ")

while z.isdigit() == False:
    z = input("Provide an integer number: ")

x = int(z)
if x % 2 == 0:
    print ("Even number.")
else:
    print ("Odd number.")