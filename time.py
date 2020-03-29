hours = int(input())
minutes = int (input ())

minutes = minutes + 15

if minutes >= 60:
    minutes = minutes - 60
    hurs = hours + 1

if hours == 24
    hours = 0

print (f"{hours}:{minutes:02d}")