import os

   # File to store tasks
TASKS_FILE = 'tasks.txt'

def load_tasks():
       """Load tasks from the text file."""
       if os.path.exists(TASKS_FILE):
           with open(TASKS_FILE, 'r') as file:
               return [line.strip() for line in file.readlines()]
       return []

def save_tasks(tasks):
       """Save tasks to the text file."""
       with open(TASKS_FILE, 'w') as file:
           for task in tasks:
               file.write(task + '\n')

def add_task(tasks, task):
       """Add a new task to the list."""
       tasks.append(task)
       save_tasks(tasks)
       print(f'Task "{task}" added.')

def remove_task(tasks, task):
       """Remove a task from the list."""
       if task in tasks:
           tasks.remove(task)
           save_tasks(tasks)
           print(f'Task "{task}" removed.')
       else:
           print(f'Task "{task}" not found.')

def view_tasks(tasks):
       """View all tasks in the list."""
       if tasks:
           print("Your tasks:")
           for idx, task in enumerate(tasks, start=1):
               print(f"{idx}. {task}")
       else:
           print("No tasks found.")

def main():
       """Main function to run the To-Do List Application."""
       tasks = load_tasks()

       while True:
           print("\nTo-Do List Application")
           print("1. Add Task")
           print("2. Remove Task")
           print("3. View Tasks")
           print("4. Exit")
           choice = input("Choose an option (1-4): ")

           if choice == '1':
               task = input("Enter the task: ")
               add_task(tasks, task)
           elif choice == '2':
               task = input("Enter the task to remove: ")
               remove_task(tasks, task)
           elif choice == '3':
               view_tasks(tasks)
           elif choice == '4':
               print("Exiting the application.")
               break
           else:
               print("Invalid choice. Please try again.")

if __name__ == "__main__":
       main()
   