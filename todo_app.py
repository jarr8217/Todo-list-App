# Todo CLI Application
# Welcome message and menu display

tasks = ['laundry', 'grocery shopping', 'cleaning', 'exercise', 'study', 'reading', 'cooking', 'writing', 'coding']

# Main menu display 
def display_menu():
    print('\nWelcome to the Todo CLI Application!:')
    print('-------------------------------------')
    print('1: Add a task')
    print('2: View tasks')
    print('3: Delete a task')
    print('4: Exit the application')
    print('-------------------------------------')

# Function to add a task to the todo list
def add_task():
    task = input('Enter the task you want to add (max 50 characters): ').strip()

    if not task:
        print('Task cannot be empty.')
    elif len(task) > 50:
        print('Task exceeds maximum length of 50 characters.')
    else: 
        tasks.append(task)
        print(f'Task "{task}" added successfully.')

# Function to view current task list
def view_tasks():
    if not tasks:
        print('No tasks available.')
    else:
        print(f'Current to-do tasks ({len(tasks)})')
        for i, task in enumerate(tasks, 1):
            print(f'{i}. {task}')

# Function to delete a task from the todo list
def delete_task():
    if not tasks:
        print('No tasks in the todo list.')
        return

    print(f'Current to-do tasks ({len(tasks)}):')
    for i, task in enumerate(tasks, 1):
        print(f'{i}. {task}')

    try:
        idx = int(input('Enter the task number you want to delete: ')) - 1

        if 0 <= idx < len(tasks):
            task_to_delete = tasks[idx]
            print('------------------------')
            print(f'Task: "{task_to_delete}"')
            confirm = input('Are you sure you want to delete this task? (y/n): ').strip().lower()

            if confirm in ['y', 'yes']:
                tasks.pop(idx)
                print(f'Task "{task_to_delete}" deleted successfully.')
            else:
                print('Task deletion cancelled.')
        else:
            print('Invalid task number. Please try again.')

    except ValueError:
        print('Invalid input. Please enter a number.')
def main():

    while True:
        display_menu()
        user_input = input('Enter menu option(1-4):').strip()

        if not user_input.isdigit():
            print('Invalid input. Please enter a number between 1 and 4.')
            continue

        try:
            choice = int(user_input)

            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                print('Exiting the application...')
                break

        except ValueError:
            print('Invalid input. Please enter a number between 1 and 4.')

            
        


main()
