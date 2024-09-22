import FreeSimpleGUI as sg

label_file_to_compress = sg.Text("Select files to compress")
label_destination_folder = sg.Text("Select destination folder")
input1 = sg.Input()
input2 = sg.Input()
button_file_to_compress = sg.FilesBrowse("Choose")
button_destination_folder = sg.FolderBrowse("Choose")
button_compress = sg.Button("Compress")

main_window = sg.Window("File Zipper",
                        layout=[[label_file_to_compress,input1,button_file_to_compress],
                                [label_destination_folder,input2,button_destination_folder],
                                [button_compress]],
                        font=("Helvetica",200))
main_window.read()
main_window.close()
