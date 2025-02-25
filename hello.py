mport subprocess
import os

# Folder and file name
folder_name = "myfolder"  # Change this to your folder
file_name = "hello.py"

# Ensure the folder exists
os.makedirs(folder_name, exist_ok=True)

# Create full file path
file_path = os.path.join(folder_name, file_name)

# Open file in Vim
subprocess.run(["vim", file_path])

