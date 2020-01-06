import os
import time
import gc
import modules.helpers as helpers
from pydub import AudioSegment
from tqdm import tqdm

class Splitter:

	def __init__(self, path, chunklength, new_path=os.getcwd()):
		self.path = path
		self.new_path = new_path
		self.chunklength = chunklength

	def split_to_chunks(self, new_name):

		'''
		takes an original file, and splits it into chunk size in new path.

		Parameters:
		new_name (str): a new filename without extension or path

		ex: "users\\file.mp3" should be inserted as "file"
		'''

		audio_file = AudioSegment.from_mp3(self.path)

		audio_remaining = True
		beg_segment = 0

		pbar = tqdm(total=len(audio_file))

		while audio_remaining:
			end_segment = beg_segment + self.chunklength

			#if remaining audio is less than chunk size, export remaining length
			if end_segment > len(audio_file):
				remaining_audio = end_segment - len(audio_file)
				remaining_audio = remaining_audio * -1
				full_segment = audio_file[remaining_audio:]

				new_path = self.new_path + "\\" + new_name
				new_path = (new_path + "_" + str(helpers.convert_to_mins((beg_segment))) + "-" +
							str(helpers.convert_to_mins(len(audio_file))) + ".mp3")

				full_segment.export(new_path, format="mp3")

				audio_remaining = False #break
			else:
				full_segment = audio_file[beg_segment:end_segment]

				new_path = self.new_path + "\\" + new_name
				new_path = (new_path + "_" + str(helpers.convert_to_mins((beg_segment))) + "-" + 
							str(helpers.convert_to_mins((end_segment))) + ".mp3")

				full_segment.export(new_path, format="mp3")

			start = beg_segment
			beg_segment += self.chunklength #iterate

			#using this instead of regular update to make it look nicer
			helpers.incriment_pbar(start, beg_segment, pbar)

		del audio_file
		pbar.close()
		gc.collect()

def split_all(path, files_list, chunklength, new_path):

	'''
	uses split_to_chunks() to loop over all files in a list of files, and split them.
	Deletes all files in files_list when finished.

	Parameters:

	path (str): a new filename without extension or path

	files_list (list of str): list of files converted (ex: filename.mp3) 
								passed from AudioConverter.convert_all()

	chunklength (int): length per file (in milliseconds)

	new_path (str): Output directory of split files.

	'''

	print("\n\nSplitting files\n\n")	
	i = 1

	for file in files_list:

		print("splitting: {}, file {} of {}".format(file, str(i), str(len(files_list))) )

		full_path = path + "\\" + file
		file_to_split = Splitter(full_path, chunklength, new_path)

		name_without_ext = file.split(".mp3")[0]
		file_to_split.split_to_chunks(name_without_ext)

		i += 1

	delete_files(path, files_list)

def delete_files(path, files_list):

	'''
	Deletes all files from files_list in a given path (directory)

	Parameters:
    path (str): directory of files to be deleted
    files_list: list of files to delete within given directory.

	'''
	for file in files_list:
		full_path = path + "\\" + file
		if os.path.exists(full_path):
			os.remove(full_path)
			print(full_path + " removed.")


