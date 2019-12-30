import os
import time
import gc
from pydub import AudioSegment
import moviepy.editor as mp

import AudioConverter as ac_module
import Splitter as splitter_module
import helpers


if __name__ == "__main__":
	print("\n\n\n")

	path = input("Paste the directory with video files to convert: ")
	new_path = input("Paste new directory for audio files: ")
	chunklength = input("Type length of files (Format: 5.30 = 5 mins 30 sec): ")

	if new_path is '':
		new_path = path

	chunklength = int((float(chunklength) * 1000) * 60)

	print("\n\n\n" + str(chunklength) + " THIS IS THE CHUNK LENGATH WHY THO")

	print("\n\n")
	print("--------------------------------------------")
	print("\n\nconverting all video files in directory to mp3, this may take a while\n\n")
	print("--------------------------------------------")
	print("\n\n")

	files_list = ac_module.convert_all(path)

	splitter_module.split_all(path, files_list, chunklength, new_path)

	print("\n\nFinished!\n\n")