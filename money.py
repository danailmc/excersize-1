money_for_break = float(input())
current_money = float(input())

while current_money >= money_for_break:
    command = input()
    money = float(input())

    if command == "spend":
        spend_counter += 1

        spend_counter == 5:
        print ("You cant save the money.")
        print(days)
        break
        else:

            current_money -= money
            if current_money < 0
                current_money = 0
    elif command == "save":
        spend_counter = 0
        current_money += money

print(f"You saved th money for {days}days")
             

