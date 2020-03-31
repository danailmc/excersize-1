age = int(input())
washing_machine_price = float (input())
price_toy = int(input())

toys_count = 0
savings = 0
mooney_to_recieve = 0
for year in range (1, age + 1):
    if year % 2 == 0:
        toys_count += 1
    else:
        mooney_to_recieve += 10
        savings += mooney_to_recieve
        savings -= 1
savaings += toys_count * price_toy
    if savings >= washing_machine_price:
print (f "Yes! {savings - washing_machine_price: 2f}")