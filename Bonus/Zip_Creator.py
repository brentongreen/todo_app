import zipfile
import pathlib

def new_zip(selected_files,dest_folder):
    des_filepath = pathlib.Path(dest_folder, "compressed.zip")
    with zipfile.ZipFile(des_filepath,"w") as archive:
        for x in selected_files:
            x = pathlib.Path(x)
            archive.write(x, arcname=x.name)

if( __name__=="__main__"):
    new_zip(selected_files=["bonus8.py"],dest_folder="Files")