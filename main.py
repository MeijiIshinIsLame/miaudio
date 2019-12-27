import os
import time
from pydub import AudioSegment
import moviepy.editor as mp

import AudioConverter as ac_module
import Splitter as splitter_module
import helpers


if __name__ == "__main__":
	path = input("Paste the directory with video files to convert: ")
	new_path = input("Paste new directory for audio files: ")
	chunklength = input("Type length of files (Format: 5.30 = 5 mins 30 sec): ")

	if new_path is '':
		new_path = path

	chunklength = int(float(chunklength) * 100000)

	print("\n\n")
	print("--------------------------------------------")
	print("\n\nconverting all video files in directory to mp3, this may take a while\n\n")
	print("--------------------------------------------")
	print("\n\n")

	files_list = ac_module.convert_all(path)

	print(files_list)
	splitter_module.split_all(path, files_list, chunklength, new_path)