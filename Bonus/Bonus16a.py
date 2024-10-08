import FreeSimpleGUI as sg
import Zip_Creator as zc

label_file_to_compress = sg.Text("Select files to compress")
label_destination_folder = sg.Text("Select destination folder")
input1 = sg.Input(key="I_Files")
input2 = sg.Input(key="I_Folders")
button_file_to_compress = sg.FilesBrowse("Choose", key="B_Files")
button_destination_folder = sg.FolderBrowse("Choose", key="B_Folders")
button_compress = sg.Button("Compress")
output = sg.Text()

main_window = sg.Window("File Zipper",
                        layout=[[label_file_to_compress,input1,button_file_to_compress],
                                [label_destination_folder,input2,button_destination_folder],
                                [button_compress,output]],
                        font=("Helvetica",20))

while True:
    event, values = main_window.read()
    print(event,values)
    files_list = values["B_Files"].split(";")
    folder = values["B_Folders"]
    print(files_list)
    print(folder)
    zc.new_zip(files_list,folder)
    output.update(value="File Compressed")
main_window.close()
