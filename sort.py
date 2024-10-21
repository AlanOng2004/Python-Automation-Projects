import os
import shutil

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

folders = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xls', '.xlsx', '.pptx'],
    'Videos': ['.mp4', 'mkv', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.7z'],
    'Others': []
}

for folder in folders.keys():
    folder_path = os.path.join(desktop_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def move_files():
    for filename in os.listdir(downloads_path):
        if os.path.isdir(os.path.join(downloads_path, filename)):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        for folder, extensions in folders.items():
            if file_ext in extensions:
                shutil.move(os.path.join(downloads_path, filename), os.path.join(desktop_path, folder, filename))
                moved = True
                break

        if not moved:
            shutil.move(os.path.join(downloads_path, filename), os.path.join(desktop_path, 'Others', filename))

if __name__ == "__main__":
    move_files()
    print("Desktop cleaned and files organized")