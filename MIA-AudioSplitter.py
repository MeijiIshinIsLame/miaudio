import os
import time

import AudioConverter as ac_module
import Splitter as splitter_module
import helpers


if __name__ == "__main__":
	print("\n\n\n")

	getting_input = True

	while getting_input:
		path = input("Paste the directory with video files to convert: ")
		if os.path.isdir(path):
			break
		else:
			print("\nERROR: Specified directory does not exist, please try again.\n")


	new_path = input("Paste new directory for audio files: ")


	while getting_input:
		chunklength = input("Type length of files (Format: 5:30 = 5 mins 30 sec): ")
		chunklength = helpers.convert_to_milliseconds(chunklength)

		if chunklength == -1:
			print("Length incorrect, please try again.")
		else:
			break


	if new_path == '':
		new_path = path
	else:
		helpers.create_directory_if_none(new_path)


	print("\n\n")
	print("--------------------------------------------")
	print("\n\nconverting all video files in directory to mp3, this may take a while\n\n")
	print("--------------------------------------------")
	print("\n\n")

	files_list = ac_module.convert_all(path)

	splitter_module.split_all(path, files_list, chunklength, new_path)

	print("\n\nFinished!\n\n")