import moviepy.editor as mp
import os

class AudioConverter:

	def __init__(self, path):
		self.path = path

	def convert_to_audio(self):
		clip = mp.VideoFileClip(self.path)

		new_name = os.path.splitext(self.path)[0] + ".mp3"
		clip.audio.write_audiofile(new_name)

		#close file
		del clip.reader
		del clip

		return new_name

def convert_all(path):
	extensions = {".mp4", ".wmv", ".avi", ".webm", ".mkv"}
	files_converted = []

	for file in os.listdir(path):
		for filetype in extensions:
			if file.endswith(filetype):
				mp3_file = file.split(filetype)[0] + ".mp3"
				if (mp3_file) not in os.listdir(path):
					video_to_convert = AudioConverter(path + "\\" + file)
					video_to_convert.convert_to_audio()
					files_converted.append(mp3_file)

	#actually, return a list with the mp3 instead, not te original file. what the fk was i thinking tbh.
	return files_converted