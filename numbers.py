count_numbers = int(input())

biggest_number = 0
smallest_number = 0
for position in range (count_numbers):
    curent_number = int (input())
    if position == 0:
        biggest_number = curent_number
        smallest_number = curent_number
    else:
        if curent_number > biggest_number:
            biggest_number = curent_number
            elif curent_number < smallest_number
                smallest_number = curent_number

    print (f "biggest: {biggest_number}, smallest: {smallest_number})