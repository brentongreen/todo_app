import functions
import FreeSimpleGUI as sg

label = sg.Text("Please enter your to do :")
input_box =sg.InputText(tooltip="Enter to do",key="Todo")
add_button =sg.Button("Add")
edit_button =sg.Button("Edit")
complete_button = sg.Button("Complete")
list_box =sg.Listbox(values=functions.get_todos(),
                     key="Todos",
                     enable_events=True,
                     size=[45,10])

window = sg.Window("This is Brenton's to do list of to do app",
                   layout=[[label],[input_box,add_button],[list_box,edit_button]],
                   font=("Helvetica",20))

print(window.read())

while True:
    event, values = window.read()

    match event:
        case'Add':
            todos = functions.get_todos()
            new_todo = values['Todo']+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["Todos"].update(values=todos)

        case'Complete':
            print("Complete")
        case 'Exit':
            break
        case 'Edit':
            new_todo = values["Todo"]
            old_todo = values["Todos"][0]
            todos=functions.get_todos()
            edit_index = todos.index(old_todo)
            todos[edit_index] = new_todo +"\n"
            functions.write_todos(todos)
            window["Todos"].update(values=todos)

        case 'Todos':
            window["Todo"].update(value=values["Todos"][0])

        case sg.WINDOW_CLOSED:
            break

window.close()