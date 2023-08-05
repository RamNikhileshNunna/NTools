import os
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