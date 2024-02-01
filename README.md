# Directory Monitor Script

<p >
<img src="https://media.tenor.com/8EszoDmZaa8AAAAi/superman-flying.gif">
</>

## Overview

This Python script monitors a specified directory or you full system directory for new and deleted files or folders and sends notifications using the `plyer` library. Additionally, it copies the file path to the clipboard for easy access.

## Prerequisites

- Python 3.x
- `plyer` library: Install using `pip install plyer`
- `pyperclip` libary: Install using `pip install pyperclip`

## Usage

1. Clone or download the repository to your local machine using `git` or download `zip` file.

2. Open a terminal and navigate to the directory containing the script.

3. Run the script by entering the following command:

   ```bash
   python main.py
   
4. Enter the base directory path.

5. The script will start monitoring the specified directory, and you will receive notifications for new and deleted files or folders.
6. **you can set this script on startup , then when you system is start the script will automaticly exicute and run on background**


## Notifications

### New File or Folder Notification:
- Title: New File or Folder Come
- Message:
   ```bash
   New File or Folder:
   Name: [file or folder path]
   
   File path is copied to clipboard.
   ```

### Deleted File or Folder Notification:
- Title: File or Folder Deleted
- Message:

   ```bash
   File or Folder Deleted:
   Name: [file or folder path]
   
   File path is copied to clipboard.
   ```


Notes
- The script uses the plyer library for notifications, ensure it is installed before running the script.

- Make sure to provide the correct base directory path when prompted.

- The script runs indefinitely and checks for changes every 5 seconds.

- Press Ctrl+C to stop the script.

### License
- This script is licensed under the `MIT License`
