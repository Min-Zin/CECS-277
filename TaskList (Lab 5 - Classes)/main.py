#Names: Min, Hollie
"""
Description: A program that maintains a task list for the user.
The user should be able to view the current task, mark the task complete,
postpone the current task, ror add a new task. The program will read the 
list from a file ('tasklist.txt') when the program begins and then stores 
the updated list by overwriting the old contents when the user quits 
the program.
"""
from task import Task
import check_input

def main_menu(tasklist):
    # Displays the main menu and returns the user's valid input.
    print('-Tasklist-')
    print(f'You have {len(tasklist)} tasks.')
    print('1. Display current task\n2. Mark current task complete\n3. Postpone current task\n4. Add new task\n5. Save and quit')

    choice = check_input.get_int_range('Enter choice: ', 1, 5)
    return choice

def read_file():
    # Opens the file ('tasklist.txt') and read each of the tasks.
    # Construct a task object from each line adn add it to a list.
    # Return the filled task list.
    tasklist = []
    with open('tasklist.txt', 'r') as file:
        for line in file: #loops through each line in the file
            desc, date, time = line.strip().split(',') 
            tasklist.append(Task(desc,date,time)) # makes a task obj and adds to list
        return tasklist
    
    
def write_file(tasklist):
    # Passes in the list of tasks that will be written to the file
    # ('tasklist.txt'). Iterate through the list of tasks and write each
    # one to the file using the Task's repr() method
    with open('tasklist.txt', 'w') as file: # opens for writing and overwrites 
        for task in tasklist:
            file.write(task.__repr__() + '\n') # writes the task using repr() and adds a new line
            

def get_date():
    # Prompt the user to input a month, day, and year
    # Valid: year (2000 - 2100), month (1 - 12), day (1 - 31)
    # Return the date in the format: MM/DD/YYYY
    # If the inputted month or day is less than 10, add a leading 0 to format it correctly
    year = check_input.get_int_range('Enter year (2000 - 2100): ', 2000, 2100)
    month = check_input.get_int_range('Enter month (1 - 12): ', 1, 12)
    day = check_input.get_int_range('Enter day (1-31): ', 1, 31)

    formated_month = str(month).zfill(2)
    formated_day = str(day).zfill(2)

def get_time():
    # Prompts the user to enter the hour (Military time) and minute.
    # Valid: hours (0 - 23), minutes (0-59)
    # Return date in format: MM/DD/YYYY
    # If the inputted hour or minute is less than 10, add a leading 0 to format it correctly
    hour = check_input.get_int_range('Enter hour (0 - 23): ', 0, 23)
    minute = check_input.get_int_range('Enter minute (0 - 59): ', 0, 59)

    formated_hour = str(hour).zfill(2)
    formated_minute = str(minute).zfill(2)

    return f"{formated_hour}:{formated_minute}"

def main():
    tasklist = read_file()
    choice = main_menu(tasklist)
    while choice != 5:
        if choice == 1:
            print('Current task is:')
            print(tasklist[0])
        elif choice == 2:
            print(f'Marking current task as complete: {tasklist[0]}')
            tasklist.pop(0)
            print(f'New current task is: {tasklist[0]}')
        elif choice == 3:
            print('Postponing task:')
            print(tasklist[0])
            print('Enter new due date:')
            new_date = get_date()
            new_time = get_time()
            tasklist[0].date = new_date
            tasklist[0].time = new_time
        elif choice == 4:
            desc = input('Enter a task: ')
            print('Enter due date:')
            date = get_date()
            time = get_time()
            tasklist.append(Task(desc, date, time))
        
        choice = main_menu(tasklist)
    print("Saving and exiting.")
    write_file(tasklist)

main() 