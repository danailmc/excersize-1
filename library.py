book = input()
count_of_books = int(input())

counter = 0
is_found = False
while counter < count_of_books and not is_found:
    current_book = input()

    if current_book == book:
        print(f"You checked {counter}books and foun it")
        is_found = True
        counter += 1

if not is_found:
    print("The book you search is not here!")
    print(f"You checked {counter} books")
