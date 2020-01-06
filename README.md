# subs2srs-splitter-replacement
Takes a folder of video files, converts them to audio, and splits them into segments determined by the user.

#### Installation

Download here! (not uploaded yet cuz not finished lol)

1. Unzip file

in command line:
```
cd [location of folder]
pip install -r requirements.txt
python miaudio.py
```

or just clone this repo
```
git clone https://github.com/MeijiIshinIsLame/subs2srs-splitter-replacement
cd subs2srs-splitter-replacement
pip install -r requirements.txt
python miaudio.py
```

##### WARNING

This module requires 64 BIT Python 3.6.x or above!
I found out that the pydub module works with audio in RAM. If you are using a modern computer and a 64-bit version of python this should be fine, but if you are working with videos more than 30 minutes YOU WILL LIKELY RUN OUT OF MEMORY on 32-BIT VERSIONS OF PYTHON!

##### requirements
```
moviepy
pydub
tqdm
configparser
```
