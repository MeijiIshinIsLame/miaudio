import os
import helpers
from pydub import AudioSegment

class Splitter:

	def __init__(self, path, chunklength):
		self.path = path
		self.chunklength = chunklength

	def split_to_chunks(self, new_name, ext):
		audio_file = AudioSegment.from_file(self.path, ext)

		audio_remaining = True
		beg_segment = 0

		while audio_remaining:
			end_segment = beg_segment + self.chunklength

			name = new_name + "_" + str(helpers.convert_to_mins((beg_segment))) + "-" + str(helpers.convert_to_mins((end_segment)))
 
			if end_segment > len(audio_file):
				remaining_audio = end_segment - len(audio_file)
				remaining_audio = remaining_audio * -1
				full_segment = audio_file[remaining_audio:]

				name = new_name + "_" + str(helpers.convert_to_mins((beg_segment))) + "-" + str(helpers.convert_to_mins(len(audio_file)))

				name = name + "." + ext

				full_segment.export(name, format=ext)
				audio_remaining = False #break
			else:
				full_segment = audio_file[beg_segment:end_segment]
				name = name + "." + ext
				full_segment.export(name, format=ext)

			beg_segment += self.chunklength #iterate

def split_all(path, files_list, chunklength):
	pass

def delete_files(files_list):
	pass


split = Splitter("20180927_161157.mp3", 5000)
split.split_to_chunks("aaa", "mp3")


