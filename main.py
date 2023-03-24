hour = int(input("Enter the hour in 12 hour clock system\n"))
min = int(input("Enter the minutes\n"))
# Validating the time given
if hour >12:
    print("Enter valid hour")
elif min > 60:
    print("Enter valid minutes")
else:
    print("you've entered the time",hour,":",min)
# Calculating the difference between the hour hand and minute hand
angle = abs((((min/60) + hour) * 30) - (min/60 * 360))
if angle == 360:
    print("The angle difference between the hour hand and minute hand is 0.0")
else:
    print("The angle difference between the hour hand and minute hand is", angle)

