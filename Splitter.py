import os
import helpers
import time
from pydub import AudioSegment

class Splitter:

	def __init__(self, path, chunklength, new_path=os.getcwd()):
		self.path = path
		self.new_path = new_path
		self.chunklength = chunklength

	'''
	takes an original file, and splits it into chunk size in new path.

	new_name - a new filename without extension or path

	ex: "users\\file.mp3" should be inserted as "file"
	'''

	def split_to_chunks(self, new_name):

		ext = "mp3"

		audio_file = AudioSegment.from_file(self.path, ext)

		audio_remaining = True
		beg_segment = 0

		while audio_remaining:
			end_segment = beg_segment + self.chunklength

			#if remaining audio is less than chunk size, export remaining length
			if end_segment > len(audio_file):
				remaining_audio = end_segment - len(audio_file)
				remaining_audio = remaining_audio * -1
				full_segment = audio_file[remaining_audio:]

				new_path = self.new_path + "\\" + new_name
				print("new name: " + new_name)
				print("new_path:", self.new_path)
				new_path = new_path + "_" + str(helpers.convert_to_mins((beg_segment))) + "-" + str(helpers.convert_to_mins(len(audio_file))) + "." + ext

				full_segment.export(new_path, format=ext)

				audio_remaining = False #break
			else:
				full_segment = audio_file[beg_segment:end_segment]

				new_path = self.new_path + "\\" + new_name
				new_path = new_path + "_" + str(helpers.convert_to_mins((beg_segment))) + "-" + str(helpers.convert_to_mins((end_segment))) + "." + ext

				full_segment.export(new_path, format=ext)

			beg_segment += self.chunklength #iterate

def split_all(path, files_list, chunklength, new_path=os.getcwd()):
	for file in files_list:
		print("splitting: " + file)

		full_path = path + "\\" + file
		print("\n\n\nFULL PATH: ", full_path, "\n\n\n")
		file_to_split = Splitter(full_path, chunklength, new_path)

		name_without_ext = file.split(".mp3")[0]
		file_to_split.split_to_chunks(name_without_ext)

	#you need to find the extension somehow
	delete_files(path, files_list)

#because my own dumb ass this deletes the FILES IN THE LIST
#it needs to delete the mp3 files, so make them mp3 boi
def delete_files(path, files_list):
	for file in files_list:
		if ".mp3" in file:
			full_path = path + "\\" + file
			if os.path.exists(full_path):
				os.remove(full_path)
				print(full_path + " removed.")


