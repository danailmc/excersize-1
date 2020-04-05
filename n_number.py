n = int(input())

sum_numbs = 0
max_num = -sys.maxsize
for i in range (n):
    number = int(input())

    sum_numbs += number

    if number > max_num:
        max_num = number


sum_numbs -= max_num

if max_nums == sum_numbs:
    print(f"Yes\nSum = {sum_numbs}"):
else:
    print(f"No\nDiff = {abs (sum_numbs - max_num)}")
