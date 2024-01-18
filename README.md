# xai-RF-android-detector
Welcome to my project, this is about a Random Forest model trained to classify android .apk file as malicious or benign, with XAI Shap applied (not completed in testing)
## How to use
To run this project you need to do 2 things
+ Pull and follow instructions to use [AndroPyTool](https://github.com/alexMyG/AndroPyTool). Note that AndroPyTool is run on Python 2.
+ Then pull my project

To pull my project: 

`git clone https://github.com/P0uut/xai-RF-android-detector.git`

After that please replace `APT_6_feat_extraction.py` file in this repository to the file with the same name in AndroPyTool directory. I fixed and adjusted for my PC weak compability issue, and in my current research domain. 

To install requirements and dependencies: 

`pip install requirements.txt`

This repository already has my trained Random Forest model, it's stored in `trained_rf_model.joblib` and is ready to load and use to classify .apk file.

The model was trained with 1200 benign and 1200 malicious files collected from [MalDroid2020](http://205.174.165.80/CICDataset/MalDroid-2020/Dataset/APKs/). Link source: [CIC](https://www.unb.ca/cic/datasets/maldroid-2020.html).

If you wish to train your own model, please use `in_training.ipynb` yourself and modify at your own risk, each cell of codes does different task, change them to make it yours, then save your trained model to a new .joblib file or overwrite mine.

`ready_for_detect.py` is the main script to classify .apk file using the stored trained model in the same repository. Run `python3 ready_for_detect.py -h` to see all arguments to provides.

usage: `ready_for_detect.py [-h] -eP ENVACTIVATEPATH -aP ANDROPYTOOLPATH -fP FOLDERAPKPATH -csv CSVNAME [-ext]`

Run apk detector with four arguments.

optional arguments:

+  `-h, --help`            show this help message and exit

+  `-eP ENVACTIVATEPATH`, `--envactivatePath ENVACTIVATEPATH`
                        Enter the path of your virtual environment for
                        AndroPyTool to run                      

+  `-aP ANDROPYTOOLPATH`, `--andropytoolPath ANDROPYTOOLPATH`
                        Enter the path of your AndroPyTool script

+  `-fP FOLDERAPKPATH`, `--folderapkPath FOLDERAPKPATH`
                        Enter the path of your apk folder

+  `-csv CSVNAME`, `--csvName CSVNAME`
                        Enter the name of the feature csv file

+  `-ext`, `--apkextension`  Some malicious apk may not have .apk extension, use
                        this to add .apk to the end of those file, else
                        AndroPyTool wont be able to process

> [!NOTE]
> This project is merely a scrap to those who're a ML expert, ML specialists in their major so don't expect something from here, just take it for ML implementation example