# Egg Counter Tool
Counting eggs manually can be a tiring procedure necessary for biological experiments. This tool allows researchers to count eggs laid within a petridish or vial using [OpenCV's pre-trained AI library for blob detection](https://learnopencv.com/blob-detection-using-opencv-python-c/) without much coding experience needed.

It is rudimentary by coding standards, so do understand that the UI can be _very_ clunky. At some point I might build a web application version so that it's much more accessible for all.

## <a name="Generate"></a>Generating the Executable
If you have already received a copy of the executable file (`.exe` or `.app`) from another researcher, skip down to (Running the tool)[#Running] as you won't be needing this section. Otherwise, don't worry! There aren't _too many_ steps involved. Alternatively, hand the laptop over to your programmer friend so they can set it up for you! You will need your computer's Shell terminal to run these commands. The code snippets below are written based on the MacOS Terminal, so do let me know if the commands are different for Windows!

Alternatively, might I recommend... [GitBash](https://git-scm.com/downloads), the commands are the same as what you'd have on a Unix system (MacOS/Linux).

### 1. [Install Python3](https://realpython.com/installing-python/)
One would expect the computer to come pre-installed with the latest version of Python. One might find themselves very disappointed.

### 2. [Install pip](https://pip.pypa.io/en/stable/installation/)

### 3. Install dependencies
To run the script, you will need the following:

- tkinter, which gives you the UI to interact with
    ```pip install tk```
- opencv, for the pre-trained AI
    ```pip install opencv-python```
- numpy, for math and imaging... stuff.
    ```pip install numpy```
- to generate the executable for Windows
    ```pip install pyinstaller```

### 4. Build the executable

#### Windows
Run `main.py` with pyinstaller's command, using the `--one-file` command to wrap the whole package.
```pyinstaller main.py --hidden-import cv2, --hidden-import numpy, --hidden-import math, --hidden-import os, --onefile```

#### MacOS
At the moment I have no way of generating an app file for MacOS. I attempted to use py2app but I encountered errors that appeared to have been deprecation errors according to answers on StackOverflow.

## <a name="Running"></a>Running the tool
If you don't have a copy of the executable file yet (`.exe` or `.app`), you can generate your own following the steps in (Generating the Executable)[#Generate].

### Windows
You can double-click the `.exe` file to run the executable on Windows. If a prompt appears warning you about the risks of running an executable from an unknown source, click on `See More` or `More Info` (or something along those lines) which should make the `Run Anyway` button appear.

You will need to have an `input` and `output` folder created in the same folder as the executable, with your images pasted in the `input` folder.

### MacOS
If you already know how to navigate your way with Terminal then skip directly to Step 7

1. Launch Terminal. You can find it in the Applications > Utilities folder
2. Run `open .`
3. Run `mkdir egg_counter` to create a folder called egg_counter here
4. Drag and drop `main.py` and `blob_counter.py` into the egg_counter folder that you have just created
5. Create a folder named `input` and a folder named `output`, and drag your images into the input folder
6. Run `cd egg_counter` to enter the folder on Terminal
7. Run `python3 main.py`

## Preview and Output
The tool itself is made to be human-readable (parameters like Alpha and Gamma have been translated to Contrast and Brightness), albeit rudimentary in its UI design. 

The `Preview` button will show what happens after the first image has been adjusted for computer vision, had the "blobs" detected, counted, and circled with the count indicated at the top left hand corner. You can click on the Preview button multiple times to judge the differences from your adjustments.

| :warning: NOTE                                                                                                          |
|:------------------------------------------------------------------------------------------------------------------------|
| You may want to note down the parameters you have set at this point, as those values are **NOT** stored by the program. |

When you are satisified with the parameters that you have set, click on the `Batch Process` button. The program might seemingly freeze while it is processing the images depending on the number of images it has to process. This is normal and expected. Once it has completed the batch processing, the program will close itself (without warning) and you can review the images in the `output` folder.

A `count_results.csv` file will also be added into the `output` folder, which you can open with a spreadsheet editor program. This will allow you to much more easily fix the mistakes in counting that the tool has made, and access the data for analysis.

## Changes
An option has been added since [Tahlia's Paper](https://pubmed.ncbi.nlm.nih.gov/39106944/): You can now enable/disable a checkbox that decides whether or not to count blobs that have been detected on the outside of the large main circle (usually the base of the plate).

## For Developers and Scripters
`main.py` runs the UI that allows users to adjust parameters without having to touch the code and might not be very informative. Most of the script logic can be found within `blob_counter.py`. 
