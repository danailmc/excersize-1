type_screening = input()
rows = int (input()) 
cows = int (input())
price = 0

if (type_screening == "Premiere")
    price = 12
elif type_screening == "Discount"
    price = 5
else:
    price = 7.5

ressult = price*cows*rows
print (f"{result:.2f}leva")