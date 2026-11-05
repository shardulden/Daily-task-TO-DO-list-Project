# Simple To-Do List Project

tasks = []

# Try to read old tasks from the file if it exists
try:
    file = open("tasks.txt", "r")
    for line in file:
        tasks.append(line.strip())
    file.close()
except:
    # If file doesn't exist yet, we just start fresh
    pass

# Main program loop
while True:
    print("\n=== MY TO-DO LIST ===")
    print("1. View my tasks")
    print("2. Add a new task")
    print("3. Remove a task")
    print("4. Save and Exit")

    choice = input("\nChoose an option (1-4): ")

    # Option 1: Show tasks
    if choice == "1":
        if len(tasks) == 0:
            print("You have no tasks right now!")
        else:
            print("\nHere are your tasks:")
            count = 1
            for item in tasks:
                print(str(count) + ". " + item)
                count = count + 1

    # Option 2: Add task
    elif choice == "2":
        new_item = input("What do you need to do? ")
        tasks.append(new_item)
        print("Got it, added to your list!")

    # Option 3: Delete task
    elif choice == "3":
        if len(tasks) == 0:
            print("Nothing to delete, your list is already empty.")
        else:
            print("\nWhich one did you finish?")
            count = 1
            for item in tasks:
                print(str(count) + ". " + item)
                count = count + 1

            num = int(input("\nEnter task number: "))
            
            # Check if the number is actually on the list
            if num >= 1 and num <= len(tasks):
                removed = tasks.pop(num - 1)
                print("Nice! Removed: " + removed)
            else:
                print("That number isn't on your list.")

    # Option 4: Save everything and quit
    elif choice == "4":
        file = open("tasks.txt", "w")
        for item in tasks:
            file.write(item + "\n")
        file.close()
        print("All your tasks are saved. See you later!")
        break

    else:
        print("Invalid choice, please type 1, 2, 3, or 4.")
