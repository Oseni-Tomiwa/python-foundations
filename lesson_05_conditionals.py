target_hours = 5

completed_hours = int(input("How many hours did you study today? "))

if completed_hours >= target_hours:
    print("Target hit. Good work.")
elif completed_hours > 0:
    print("You studied, but you are below your target.")
else:
    print("No study logged today. Reset and start again.")