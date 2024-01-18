import os
import time
import shap
import joblib
import argparse
import subprocess
import pandas as pd
import numpy as np
from apk_ext_rename import rename_files
from sklearn.model_selection import *
from sklearn.metrics import *

def run_feature_shell_script(arg1, arg2, arg3, arg4, arg5=False):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    shell_script_path = os.path.join(current_directory, 'feature_extractor.sh')
    print(f'Working shell script path: {shell_script_path}')

    # Cell to initiate the virtual environment and run the AndroPyTool
    try:
        # Run the shell script with the provided arguments
        # example_path = '/home/android/project/example.sh'
        #arg1 = '/home/android/droidbox_env/bin/activate' ### Change this to your env activate script
        #arg2 = '/home/android/AndroPyTool/androPyTool.py' ### Change this to your androPyTool.py script
        #arg3 = '/home/android/Desktop/Mal_Ben/' ### Change this to your apk folder that you want to test
        #arg4 = 'extracted_feature.csv' ### Name of the feature file
        print(f'Working shell script path: {shell_script_path}')
        if arg5 is not False:
            rename_files(arg3)
        result = subprocess.run([shell_script_path, arg1, arg2, arg3, arg4], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # print("Script output:", result.stdout)
        for line in result.stdout.splitlines():
            line = line.decode('utf-8').strip()
            print(line)

        for line in result.stderr.splitlines():
            line = line.decode('utf-8').strip()
            print(line)
        while (not os.path.exists(os.path.abspath(arg3 + 'Features_files/' + arg4))):
            print("Waiting for feature extraction process...")
            time.sleep(10)
        predict(os.path.abspath(arg3 + 'Features_files/' + arg4))

    except subprocess.CalledProcessError as e:
        print("Error running script:", e)
        print("Script error output:", e.stderr)

def predict(path):
    # Load the trained Random Forest model
    current_directory = os.path.dirname(os.path.abspath(__file__))
    model_filename = os.path.join(current_directory, 'trained_rf_model.joblib')
    trained_model = joblib.load(model_filename)
    data = pd.read_csv(path)
    # Drop columns
    X = data.drop(["label", "APK Name"], axis=1)

    # Load the CSV file used during training
    training_csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_no_package.csv')
    training_data = pd.read_csv(training_csv_path)
    training_data = training_data.drop(["label", "APK Name"], axis=1)

    # Get the feature names used during training
    trained_feature_names = training_data.columns.tolist()

    # Extract common features between the new data and the trained model
    common_feature_names = set(X.columns) & set(trained_feature_names)

    # Filter the new data to keep only common features
    new_data_filtered = X[list(common_feature_names)]

    # Get the feature names expected by the trained model
    expected_feature_names = trained_feature_names

    # Pad the new data with zeros for missing features
    missing_features = set(expected_feature_names) - set(new_data_filtered.columns)
    for feature in missing_features:
        new_data_filtered[feature] = 0

    # Reorder columns to match the expected feature order
    new_data_filtered = new_data_filtered[expected_feature_names]

    print(new_data_filtered.head())
    new_data_filtered.to_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "see.csv"), index=False)
    # Make predictions using the filtered and padded data
    predictions = trained_model.predict(new_data_filtered)

    # Print predictions with corresponding APK file names
    for apk_name, prediction in zip(data["APK Name"], predictions):
        print(f"APK: {apk_name}, Predicted Label: {prediction}")
    #shap_explainer(trained_model, X, predictions, data)
        

# Temporary scrap
def shap_explainer(trained_model, X, predictions, data):
    # Initialize the SHAP explainer with the trained model
    explainer = shap.TreeExplainer(trained_model)
    print("88")
    # Calculate SHAP values for each instance in the new data
    shap_values = explainer.shap_values(X)
    print("91")
    # Print out the 3 most important features for each instance
    for i in range(len(predictions)):
        apk_name = data["APK Name"].iloc[i]
        prediction = predictions[i]
        shap_values_instance = shap_values[prediction][i, :]
        
        print(f"APK: {apk_name}, Predicted Label: {prediction}")
        
        # Print the top 3 most important features
        feature_importance = pd.Series(shap_values_instance, index=X.columns)
        top_features = feature_importance.abs().nlargest(3)  # Select the top 3 features
        print("Top 3 Features:")
        print(top_features)
        print()


def main():
    parser = argparse.ArgumentParser(description='Run apk detector with four arguments.')
    parser.add_argument('-eP','--envactivatePath', required=True, help='Enter the path of your virtual environment for AndroPyTool to run')
    parser.add_argument('-aP','--andropytoolPath', required=True, help='Enter the path of your AndroPyTool script')
    parser.add_argument('-fP','--folderapkPath', required=True, help='Enter the path of your apk folder')
    parser.add_argument('-csv','--csvName', required=True, help='Enter the name of the feature csv file')
    parser.add_argument('-ext','--apkextension', action='store_true', help='Some malicious apk may not have .apk extension, use this to add .apk to the end of those file, else AndroPyTool wont be able to process')
    args = parser.parse_args()

    # Pass the arguments to the shell script
    run_feature_shell_script(args.envactivatePath, args.andropytoolPath, args.folderapkPath, args.csvName, args.apkextension)

    # Continue with the Python 3 program
    # Your code to process the generated files can go here

if __name__ == '__main__':
    main()