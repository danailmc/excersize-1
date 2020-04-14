number = input()

non_prine_sum = 0
prime_sum = 0

while number != "stop":
    number = int(number)
    if number < 0:
        print("Number is negative.")
    else:
        for i in range(2, number):
            if number % i == 0:
                non_prine_sum += number
                is_prime = False
        if is_prime:
            prime_sum += number

    number = input()
print(f"sum of all prime numbers is:{prime_sum} ")
print(f"sum of all prime numbers is:{non_prime_sum} ")