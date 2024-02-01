from plyer import notification
import os
from time import sleep
import pyperclip

def get_all_files(directory):
    all_files = []
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            all_files.append(file_path)
    return set(all_files)

def filter(directory):
    initial_files = get_all_files(directory)

    def notify(message):
        notification.notify(
            title="New File or Folder Come",
            message=message
        )

    while True:
        current_files = get_all_files(directory)

        new_files = current_files - initial_files
        deleted_files = initial_files - current_files

        if new_files:
            for new_file in new_files:
                data = f'''New File or Folder:
                Name: {new_file}
                
                file path is coppyed on clipbord
                '''
                notify(data)
                pyperclip.copy(new_file)


        if deleted_files:
            for deleted_file in deleted_files:
                data = f'''File or Folder Deleted:
                Name: {deleted_file}
                
                file path is coppyed on clipbord
                '''
                notify(data)
                pyperclip.copy(new_file)


        initial_files = current_files
        sleep(5)

if __name__ == '__main__':
    user_input = input("Enter the base directory path: ")
    target_directory = os.path.expanduser(user_input)  # Expand user path if '~' is used

    if not os.path.exists(target_directory):
        print(f'Directory not available: {target_directory}')
    else:
        print(f'Monitoring Directory: {target_directory}')
        filter(target_directory)
