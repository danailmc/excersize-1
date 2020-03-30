product = input()
town = input ()
quantity = float (input())

price = 0
if town == "Sofia":
    if product == "cofee":
        price = 0.5
elif product == "water":
    price = 0.8
elif town == "Plovdiv":
    pass 

total_sum = quantity * price
print (total_sum)
