# PK TODO App - Day 19 by Parshotam
tasks = []

def show_menu():
    print("\n--- PK TODO APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

while True:
    show_menu()
    choice = input("Choose: ")
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
    elif choice == "3":
        print("Allah Hafiz!")
        break