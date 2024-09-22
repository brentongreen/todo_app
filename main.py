import functions
import time

now = time.strftime("%y %B %d, %H:%M:%S")
print(now)

while True:
    user_action = input("Type add, show, edit, complete or exit : ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todos = functions.get_todos()

        todo = user_action[4:]
        todos.append(todo+'\n')
        print(f'{todo} added')
        functions.write_todos(todos)

    elif user_action.startswith("complete"):
        todos = functions.get_todos()

        remove_item = int(user_action[9:])
        todos.pop(remove_item-1)
        print("Removed")
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        new_todos = []

        for item in todos:
            new_todos.append(item.strip('\n'))

        for x , y in enumerate(new_todos):
            print(f'{x+1}-{y}')

    elif user_action.startswith("edit"):
        todos = functions.get_todos()

        edit_item = int(user_action[5:])
        edit_input = input("What would you like the changed item to be :")
        todos[edit_item - 1]= edit_input +"\n"
        functions.write_todos(todos)

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid option selected.")

print("Good Bye")