import argparse
import subprocess
import os

def run_shell_script(arg1, arg2, arg3):
    current_directory = os.getcwd()
    shell_script_path = os.path.join(current_directory, 'feature_extractor.sh')

    try:
        # Run the shell script with the provided arguments
        subprocess.run([shell_script_path, arg1, arg2, arg3], check=True, shell=True)
        print("Python 2 script completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running shell script: {e}")

def main():
    parser = argparse.ArgumentParser(description='Run Python 2 script with three arguments.')
    parser.add_argument('--arg1', required=True, help='First argument for the Python 2 script.')
    parser.add_argument('--arg2', required=True, help='Second argument for the Python 2 script.')
    parser.add_argument('--arg3', required=True, help='Third argument for the Python 2 script.')
    args = parser.parse_args()

    # Pass the arguments to the shell script
    run_shell_script(args.arg1, args.arg2, args.arg3)

    # Continue with the Python 3 program
    # Your code to process the generated files can go here

if __name__ == '__main__':
    main()
