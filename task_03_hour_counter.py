target_hours = 5

input = int(target_hours)
completed_hours = input

if {input} == 0
    print("Study target must be greater than zero.")
while target_hours < completed_hours:
    completed_hours += 1
    print(f"Hour {input} logged.")