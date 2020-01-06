import os
import time
import sys
import configparser

import modules.audioconverter as ac_module
import modules.splitter as splitter_module
import modules.helpers as helpers

def main_auto():
	config = configparser.ConfigParser()
	config.read('config.txt')
	
	input_path = config['parameters']['input_path']
	output_path = config['parameters']['output_path']
	split_length = config['parameters']['split_length']

	errors = False

	if os.path.isdir(input_path):
		pass
	else:
		print("\nERROR: Specified input directory does not exist. Make sure you are using the full path in config.txt.\n")
		errors = True

	if output_path == "\n":
		output_path = input_path
		print("\nOutput path unspecified, using input path.\n")

	if os.path.isdir(output_path):
		pass
	else:
		print("\nERROR: Invalid output path. Make sure you are using the full path in config.txt\n")
		errors = True


	chunklength = helpers.convert_to_milliseconds(split_length)

	if chunklength == -1:
		print("ERROR: Split length incorrect (Should be formatted as example: 5:00)")
		errors = True

	if errors is False:
		print("\n\n")	
		print("Input path:", input_path)
		print("Output path:", output_path)
		print("Length", split_length)

		process_files(input_path, output_path, chunklength)
	else:
		quit()

def main_without_args():
	print("\n\n\n")	

	getting_input = True

	while getting_input:
		input_path = input("Paste the directory with video files to convert: ")
		if os.path.isdir(input_path):
			break
		else:
			print("\nERROR: Specified directory does not exist, please try again.\n")


	output_path = input("Paste new directory for audio files (leave blank if none, or a new path): ")


	while getting_input:
		chunklength = input("Type length of files (Format: 5:30 = 5 mins 30 sec): ")
		chunklength = helpers.convert_to_milliseconds(chunklength)

		if chunklength == -1:
			print("Length incorrect, please try again.")
		else:
			break

	if output_path == '':
		output_path = input_path
	else:
		helpers.create_directory_if_none(output_path)

	process_files(input_path, output_path, chunklength)

def process_files(input_path, output_path, chunklength):

	print("\n\n")
	print("--------------------------------------------")
	print("\n\nconverting all video files in directory to mp3, this may take a while\n\n")
	print("--------------------------------------------")
	print("\n\n")

	files_list = ac_module.convert_all(input_path)

	splitter_module.split_all(input_path, files_list, chunklength, output_path)

	print("\n\nFinished!\n\n")

if __name__ == "__main__":
	if len(sys.argv) > 1:
		if (sys.argv[1] == "-a") or (sys.argv[1] == "--auto"):
			main_auto()
		else:
			print("ERROR: unrecognized args! (use -a or --auto to use config file)")
	else:
		main_without_args()