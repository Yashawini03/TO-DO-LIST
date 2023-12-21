import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=2)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task['title']} - {task['description']}")

def add_task(tasks, title, description):
    task = {'title': title, 'description': description}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

def update_task(tasks, index, title, description):
    if 1 <= index <= len(tasks):
        tasks[index - 1]['title'] = title
        tasks[index - 1]['description'] = description
        save_tasks(tasks)
        print("Task updated successfully.")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\n===== To-Do List =====")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("0. Exit")

        choice = input("Enter your choice (0-3): ")

        if choice == '0':
            break
        elif choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(tasks, title, description)
        elif choice == '3':
            display_tasks(tasks)
            index = int(input("Enter the index of the task to update: "))
            title = input("Enter new task title: ")
            description = input("Enter new task description: ")
            update_task(tasks, index, title, description)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
