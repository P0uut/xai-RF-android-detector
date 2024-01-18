import os
import argparse

def rename_files(folder_path):
    try:
        # Get a list of all items (files and directories) in the specified folder
        items = os.listdir(folder_path)

        # Iterate through each item
        for item in items:
            # Construct the full path for the item
            item_path = os.path.join(folder_path, item)

            # Check if the item is a file (not a directory)
            if os.path.isfile(item_path):
                if not item.endswith(".apk"):
                    # Generate the new file name by shifting the dot and adding ".apk"
                    new_name = item.replace(".", "") + ".apk"

                    # Construct the full paths for the old and new file names
                    old_path = item_path
                    new_path = os.path.join(folder_path, new_name)

                    # Rename the file
                    os.rename(old_path, new_path)

                    print(f"Renamed: {item} -> {new_name}")

        print("Renaming completed.")

    except Exception as e:
        print(f"An error occurred: {e}")
'''
def main():
    parser = argparse.ArgumentParser(description="Rename files in a folder by shifting the dot and adding '.apk'.")
    parser.add_argument("--folder_path",required=True, help="Path to the folder containing files to be renamed")

    args = parser.parse_args()

    folder_path = args.folder_path

    # Check if the specified path is a directory
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        exit(1)

    # Call the function to rename files
    rename_files(folder_path)

if __name__ == "__main__":
    main()
'''