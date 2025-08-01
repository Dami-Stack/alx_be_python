task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print("Reminder: '" + task + "' is a high priority task that requires immediate attention today!")
        else:
            print("Note: '" + task + "' is a high priority task. Try to complete it soon.")
    case "medium":
        if time_bound == "yes":
            print("Reminder: '" + task + "' is a medium priority task that requires attention today.")
        else:
            print("Note: '" + task + "' is a medium priority task. Plan to work on it when possible.")
    case "low":
        if time_bound == "yes":
            print("Reminder: '" + task + "' is a low priority task but still time-sensitive today.")
        else:
            print("Note: '" + task + "' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority entered. Please use: high, medium, or low.")