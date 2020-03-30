degrees = int (input())
time_of_day = input ()
outfit = ""
shoes = ""

if time_of_day == "Morning"
    if 10 <= degrees <= 18
        outfit = "sweatshirt"
        shoes = "sneakers"
    elif 18< degrees <= 24:
         outfit = "shirt"
        shoes = "Moccasins"
    else:
        outfit = "T-shirt"
        shoes = "Sandals"
elif time_of_day == "Afternoon"
    if 10 <= degrees <= 18
        outfit = "swimsuit"
        shoes = "Barefoot"
    elif 18< degrees <= 24:
         outfit = "shirt"
        shoes = "Moccasins"
    else:
        outfit = "T-shirt"
        shoes = "Sandals"
else:
    outfit = "shirt"
    shoes = "Moccasins"

print (f"Its {degrees}, get your {outfit} and {shoes}")