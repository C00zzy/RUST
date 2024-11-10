# Todo List App

todo_list_dict = {}


def list_todo_list():
    if not todo_list_dict:  # Check if dictionary is empty
        print("There are no tasks currently.")
        main_menu()
    else:
        print("\nCurrent Tasks:")
        for task, date in todo_list_dict.items():
            print(f"- {task} at {date}")
            main_menu()



def add_to_list():
    while True:
        task = input("What is your task today ")


        if task.lower() == 'q':
            main_menu()
            break

        date = input('What time? ')

        todo_list_dict[task] = date

        for task, date in todo_list_dict.items():
            print(f"- {task} at {date}")

def remove_from_list():
    task_to_remove = input("what task")

    if task_to_remove in todo_list_dict:
        del todo_list_dict[task_to_remove]
        print("removed")
        main_menu()
    else:
        print("not a list")
        main_menu()

def main_menu():
    print("wtf do you wanna do")
    choice = input("What option")
    if choice == '1':
        list_todo_list()
    elif choice == '2':
        add_to_list()
    elif choice == '3':
        remove_from_list()
    else:
        print("fuck off")
        main_menu()


main_menu()