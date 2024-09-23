import functions
import FreeSimpleGUI as sg
import time

sg.theme("Blue")

label_time =sg.Text("Time",key="Clock")
label = sg.Text("Please enter your to do :")
input_box =sg.InputText(tooltip="Enter to do",key="Todo")
add_button =sg.Button("Add")
edit_button =sg.Button("Edit")
complete_button = sg.Button("Complete",key="Complete")
exit_button = sg.Button("Exit")
list_box =sg.Listbox(values=functions.get_todos(),
                     key="Todos",
                     enable_events=True,
                     size=[45,10])

window = sg.Window("This is Brenton's to do list of to do app",
                   layout=[[label_time],
                           [label],
                           [input_box,add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],
                   font=("Helvetica",20))
event, values = window.read(timeout=10)
window["Clock"].update(value=time.strftime("%y %B %d, %H:%M:%S"))
print(window.read())

while True:
    event, values = window.read(timeout=10)
    window["Clock"].update(value=time.strftime("%y %B %d, %H:%M:%S"))

    match event:
        case'Add':
            todos = functions.get_todos()
            new_todo = values['Todo']+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["Todos"].update(values=todos)

        case'Complete':
            try:
                removed_todos = values["Todos"][0]
                print(1,removed_todos)
                todos = functions.get_todos()
                todos.remove(removed_todos)
                functions.write_todos(todos)

                window["Todos"].update(values=todos)
            except IndexError:
                sg.popup("You need to select something first from the list.",
                         font=("Helvetica",20))

        case 'Exit':
            break
        case 'Edit':
            try:
                new_todo = values["Todo"]
                old_todo = values["Todos"][0]
                todos=functions.get_todos()
                edit_index = todos.index(old_todo)
                todos[edit_index] = new_todo +"\n"
                functions.write_todos(todos)
                window["Todos"].update(values=todos)
            except IndexError:
                sg.popup("You need to select something first from the list.",
                         font=("Helvetica",20))

        case 'Todos':
            window["Todo"].update(value=values["Todos"][0])

        case sg.WINDOW_CLOSED:
            break

window.close()