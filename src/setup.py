'''import os
import shutil
import time
def copy_files(drive,destination_path,file_type):
    count = 0
    for root, directories, files in os.walk(drive):
        for file in files:
            if file.endswith(file_type):
                shutil.copy(os.path.join(root, file), destination_path)
                count += 1
    print("Disk Scan completed.....")
    time.sleep(1)
    if(count != 0):
        print(count,"files copied")
    else:
        print(f'No files found with the extension "{file_type}"')
        '''
import pathlib
import shutil

def find_files(root_dir, extension):
    for path in pathlib.Path(root_dir).rglob(extension):
        yield path

def copy_files(source_dir, destination_dir, extension):
    for file_path in find_files(source_dir, extension):
        shutil.copy(file_path, destination_dir)
