import os
from datetime import datetime

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    tasks = []
    with open(FILE_NAME, "r") as f:
        for line in f:
            parts = line.strip().split('|')
            if len(parts) == 5:
                tasks.append({
                    'task': parts[0],
                    'priority': parts[1],
                    'done': parts[2] == 'True',
                    'date': parts[3],
                    'category': parts[4]
                })
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for t in tasks:
            f.write(f"{t['task']}|{t['priority']}|{t['done']}|{t['date']}|{t['category']}\n")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- 🏆 ULTIMATE TASK TRACKER ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Done")
        print("4. Remove Task")
        print("5. Clear Completed")
        print("6. Search Tasks")
        print("7. Exit")

        choice = input("\nChoose an option (1-7): ")

        if choice == '1':
            print("\nYOUR TASK LIST:")
            if not tasks:
                print("Empty! Everything is done! 🎉")
            else:
                print(f"{'No.':<4} {'Stat':<5} {'Pri':<8} {'Cat':<10} {'Task':<20} {'Due Date'}")
                print("-" * 60)
                for i, t in enumerate(tasks, 1):
                    status = "✅" if t['done'] else "⏳"
                    print(f"{i:<4} {status:<5} {t['priority']:<8} {t['category']:<10} {t['task']:<20} {t['date']}")
                print("-" * 60)

        elif choice == '2':
            name = input("Task name: ")
            print("Priority: (H)igh, (M)edium, (L)ow")
            p_choice = input("Select priority: ").upper()
            p_map = {'H': 'High', 'M': 'Medium', 'L': 'Low'}
            priority = p_map.get(p_choice, 'Medium')

            cat = input("Category (e.g. Work, Study, Home): ") or "General"
            date = input("Due Date (YYYY-MM-DD) or leave blank: ") or "No Date"

            tasks.append({'task': name, 'priority': priority, 'done': False, 'date': date, 'category': cat})
            save_tasks(tasks)
            print(f"Task '{name}' added successfully!")

        elif choice == '3':
            if not tasks:
                print("Nothing to mark done!")
                continue
            try:
                num = int(input("Task number to mark as DONE: "))
                if 1 <= num <= len(tasks):
                    tasks[num-1]['done'] = True
                    save_tasks(tasks)
                    print("Task completed! 🌟")
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
            original_count = len(tasks)
            tasks = [t for t in tasks if not t['done']]
            save_tasks(tasks)
            print(f"Cleared {original_count - len(tasks)} completed tasks! 🧹")

        elif choice == '6':
            query = input("Search for task keyword: ").lower()
            results = [t for t in tasks if query in t['task'].lower()]
            if results:
                print("\nSEARCH RESULTS:")
                for t in results:
                    print(f"- {t['task']} ({t['priority']}) | Due: {t['date']}")
            else:
                print("No matching tasks found.")

        elif choice == '7':
            print("Stay organized! Goodbye! 👋")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
