import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    tasks = []
    with open(FILE_NAME, "r") as f:
        for line in f:
            # Split the line back into its parts
            parts = line.strip().split('|')
            if len(parts) == 3:
                tasks.append({'task': parts[0], 'priority': parts[1], 'done': parts[2] == 'True'})
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for t in tasks:
            f.write(f"{t['task']}|{t['priority']}|{t['done']}\n")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- 🚀 PRO TASK TRACKER ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Done")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ")

        if choice == '1':
            print("\nYOUR TASK LIST:")
            if not tasks:
                print("Empty! Go enjoy your day! ☀️")
            else:
                print("-" * 30)
                for i, t in enumerate(tasks, 1):
                    status = "✅" if t['done'] else "⏳"
                    print(f"{i}. {status} [{t['priority']}] {t['task']}")
                print("-" * 30)

        elif choice == '2':
            name = input("What needs to be done? ")
            print("Priority: (H)igh, (M)edium, (L)ow")
            p_choice = input("Select priority: ").upper()
            p_map = {'H': 'High', 'M': 'Medium', 'L': 'Low'}
            priority = p_map.get(p_choice, 'Medium')

            tasks.append({'task': name, 'priority': priority, 'done': False})
            save_tasks(tasks)
            print(f"Added: {name} ({priority})")

        elif choice == '3':
            if not tasks:
                print("Nothing to mark done!")
                continue
            try:
                num = int(input("Task number to mark as DONE: "))
                if 1 <= num <= len(tasks):
                    tasks[num-1]['done'] = True
                    save_tasks(tasks)
                    print("Task completed! 🎉")
                else:
                    print("Invalid number!")
            except ValueError:
                print("Please enter a number!")

        elif choice == '4':
            if not tasks:
                print("Nothing to remove!")
                continue
            try:
                num = int(input("Task number to REMOVE: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num-1)
                    save_tasks(tasks)
                    print(f"Deleted: {removed['task']}")
                else:
                    print("Invalid number!")
            except ValueError:
                print("Please enter a number!")

        elif choice == '5':
            print("Keep crushing your goals! Goodbye! 👋")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
