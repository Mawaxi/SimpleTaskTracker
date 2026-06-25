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
            if len(parts) == 4:
                tasks.append({
                    'task': parts[0],
                    'priority': parts[1],
                    'done': parts[2] == 'True',
                    'due': parts[3]
                })
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for t in tasks:
            f.write(f"{t['task']}|{t['priority']}|{t['done']}|{t['due']}\n")

def get_date_status(due_date):
    try:
        today = datetime.now().strftime("%Y-%m-%d")
        if due_date == today:
            return "🚨 DUE TODAY!"
        elif due_date < today:
            return "⚠️ OVERDUE"
        return f"📅 Due: {due_date}"
    except:
        return "No date"

def main():
    tasks = load_tasks()

    while True:
        print("\n--- 🌟 ULTRA TASK TRACKER ---")
        print(f"Stats: {len(tasks)} Total | {len([t for t in tasks if t['done']])} Done")
        print("1. View All Tasks")
        print("2. Add New Task")
        print("3. Mark Task Done")
        print("4. Search Tasks")
        print("5. Remove Task")
        print("6. Exit")

        choice = input("\nChoose an option (1-6): ")

        if choice == '1':
            print("\nYOUR TASK LIST:")
            if not tasks:
                print("Everything is clear! ☀️")
            else:
                print(f"{'ID':<3} {'Status':<8} {'Priority':<10} {'Task':<20} {'Deadline'}")
                print("-" * 60)
                for i, t in enumerate(tasks, 1):
                    status = "✅" if t['done'] else "⏳"
                    date_info = get_date_status(t['due']) if not t['done'] else "Completed"
                    print(f"{i:<3} {status:<8} [{t['priority']:<8}] {t['task']:<20} {date_info}")
                print("-" * 60)

        elif choice == '2':
            name = input("Task description: ")
            print("Priority: (H)igh, (M)edium, (L)ow")
            p_choice = input("Select priority: ").upper()
            p_map = {'H': 'High', 'M': 'Medium', 'L': 'Low'}
            priority = p_map.get(p_choice, 'Medium')

            print("Enter due date (YYYY-MM-DD) or leave blank:")
            due = input("Date: ").strip()
            if not due:
                due = "No Date"

            tasks.append({'task': name, 'priority': priority, 'done': False, 'due': due})
            save_tasks(tasks)
            print(f"Successfully added: {name}")

        elif choice == '3':
            try:
                num = int(input("Task number to mark as DONE: "))
                if 1 <= num <= len(tasks):
                    tasks[num-1]['done'] = True
                    save_tasks(tasks)
                    print("Great job! Task completed! 🎉")
                else:
                    print("Invalid number!")
            except ValueError:
                print("Please enter a valid number!")

        elif choice == '4':
            query = input("Search for keyword: ").lower()
            results = [t for t in tasks if query in t['task'].lower()]
            if results:
                print("\nSearch Results:")
                for t in results:
                    status = "✅" if t['done'] else "⏳"
                    print(f"{status} {t['task']} ({t['priority']})")
            else:
                print("No matching tasks found.")

        elif choice == '5':
            try:
                num = int(input("Task number to REMOVE: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num-1)
                    save_tasks(tasks)
                    print(f"Deleted: {removed['task']}")
                else:
                    print("Invalid number!")
            except ValueError:
                print("Please enter a valid number!")

        elif choice == '6':
            print("Keep achieving greatness! Goodbye! 👋")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
