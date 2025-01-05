import os


def create_advent_folders(root_folder, extension):
    """
    Create subfolders from 01 to 25 in the root folder.
    Each folder will contain an empty programming file (e.g., 01.go) and an input file (e.g., 01-input.txt).

    Args:
        root_folder (str): The root directory where subfolders will be created.
        extension (str): The file extension for the programming file (e.g., '.go', '.py').
    """
    # Ensure the root folder exists
    os.makedirs(root_folder, exist_ok=True)

    # Iterate over folder numbers from 01 to 25
    for i in range(1, 26):
        folder_name = f"{i:02}"
        folder_path = os.path.join(root_folder, folder_name)

        # Create the subfolder if it doesn't already exist
        os.makedirs(folder_path, exist_ok=True)

        # Define file paths for the programming and input files
        prog_file = os.path.join(folder_path, f"{folder_name}{extension}")
        txt_file = os.path.join(folder_path, f"{folder_name}-input.txt")

        # Create the programming file if it doesn't already exist
        if not os.path.exists(prog_file):
            open(prog_file, "w").close()

        # Create the input file if it doesn't already exist
        if not os.path.exists(txt_file):
            open(txt_file, "w").close()

        print(f"Processed folder: {folder_name}")


if __name__ == "__main__":
    root_folder = "2015"
    extension = ".go"
    create_advent_folders(root_folder, extension)
