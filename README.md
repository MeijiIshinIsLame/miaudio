# miaudio
Takes a folder of video files, converts them to audio, and splits them into segments determined by the user.

#### Installation

1. <a href="https://drive.google.com/file/d/1xmusgLdL-jmvcXzdUYD-P47EgujrKOS2/view?usp=sharing">Download here!</a>
2. Unzip file
3. in command line:
```
cd C:\Users\path\to\miaudio
pip install -r requirements.txt
```

or just clone this repo
```
git clone https://github.com/MeijiIshinIsLame/subs2srs-splitter-replacement
cd miaudio
pip install -r requirements.txt
```
##### How to Use

If you would like to do it manually:
In command line:
```
python miaudio.py
```

If you would like to use the same input, output, and chunk length every time:
1. Open config.txt and edit the parameters
2. In command line:
```
python miaudio.py -a
```
using the ```-a``` or ```--auto``` argument pulls the parameters from config.txt so you don't have to set anything yourself.


##### WARNING

This module requires 64 BIT Python 3.6.x or above!
I found out that the pydub module works with audio in RAM. If you are using a modern computer and a 64-bit version of python this should be fine, but if you are working with videos more than 30 minutes YOU WILL LIKELY RUN OUT OF MEMORY on 32-BIT VERSIONS OF PYTHON!

##### Requirements
```
moviepy
pydub
tqdm
configparser
```
