import os
import argparse

def benign_rename_files(folder_path):
    try:
        # Get a list of all files in the specified folder
        files = os.listdir(folder_path)

        # Iterate through each file
        for file in files:
            if file.startswith("benign"):
                print(f"File {file} already starts with benign...")
                new_name = file
            else:
                new_name = "benign_" + file
            if not file.endswith(".apk"):
                # Generate the new file name by shifting the dot and adding ".apk"
                new_name = file.replace(".", "") + ".apk"
            if new_name is not file:
                # Construct the full paths for the old and new file names
                old_path = os.path.join(folder_path, file)
                new_path = os.path.join(folder_path, new_name)

                # Rename the file
                os.rename(old_path, new_path)

                print(f"Renamed: {file} -> {new_name}")
            else:
                continue

        print("Benign Renaming completed.")

    except Exception as e:
        print(f"An error occurred: {e}")

'''
def main():
    parser = argparse.ArgumentParser(description="Benign rename operation")
    parser.add_argument("--folder_path",required=True, help="Path to the folder containing files to be renamed as benign")

    args = parser.parse_args()

    folder_path = args.folder_path

    # Check if the specified path is a directory
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        exit(1)

    # Call the function to rename files
    benign_rename_files(folder_path)

if __name__ == "__main__":
    main()
'''