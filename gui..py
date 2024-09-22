from email.charset import add_alias

import functions
import FreeSimpleGUI as sg

label = sg.Text("Please enter your to do :")
input_box =sg.InputText(tooltip="Enter to do")
add_button =sg.Button("Add")
edit_button =sg.Button("Edit")
complete_button = sg.Button("Complete")


window = sg.Window("This is Brenton's to do list of to do app",layout=[[label],[input_box,add_button]])
window.read()
print("Hello")
window.close()