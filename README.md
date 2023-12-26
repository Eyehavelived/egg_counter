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
- to generate the app file for MacOS
    Why not use py2exe for generating the executable? Because... this was initially written for a Windows device only and making it available for MacOS came as an afterthought while writing this documentation.
    ```pip install py2app```

### 4. Build the executable

#### Windows
Run `main.py` with pyinstaller's command, using the `--one-file` command to wrap the whole package.
```pyinstaller main.py --onefile```

#### MacOS


## <a name="Running"></a>Running the tool
If you don't have a copy of the executable file yet (`.exe` or `.app`), you can generate your own following the steps in (Generating the Executable)[#Generate].

## For Developers and Scripters
`main.py` runs the UI that allows users to adjust parameters without having to touch the code and might not be very informative. Most of the script logic can be found within `blob_counter.py`. 