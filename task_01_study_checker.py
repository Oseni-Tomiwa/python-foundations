target_hours = 5

name = input("What is your name? ")
completed_hours = int(input("How many hours did you study today? "))

if completed_hours >= target_hours:
    print(f"{name}, you hit your study target today.")
elif completed_hours > 0:
    print(f"{name}, you studied but did not hit your target.")
elif completed_hours == 0:
    print(f"{name}, no study logged today. Start again tomorrow.")
else:
    print("Invalid study hours.")