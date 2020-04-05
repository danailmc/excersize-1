steps = 0

while steps < 10000:
    current_steps = input()

    if current_steps == "Going home":
        current_steps = int(input())
        steps += current_steps
        break

    current_steps = int(current_steps)
    steps += int(current_steps)

if steps >= 10000:
    print("Goal reached! Good job!")
else:
    print(f"{abs(current_steps - 10000)}")
