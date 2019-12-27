import os
import time
from pydub import AudioSegment
import moviepy.editor as mp

import AudioConverter as ac_module
import Splitter as splitter_module
import helpers


if __name__ == "__main__":
	path = "C:\\Users\\thequ\\Desktop\\immersion\\New_vids"
	new_path = "C:\\Users\\thequ\\Desktop\\immersion\\New_vids\\new"
	ext = "mp3"
	chunklength = int(5.0 * 10000)

	print("\n\n")
	print("--------------------------------------------")
	print("\n\nconverting all video files in directory to mp3, this may take a while\n\n")
	print("--------------------------------------------")
	print("\n\n")

	files_list = ac_module.convert_all(path, ext)

	print(files_list)
	splitter_module.split_all(path, files_list, chunklength, new_path=new_path)