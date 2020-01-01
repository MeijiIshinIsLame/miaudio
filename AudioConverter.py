import moviepy.editor as mp
import os

class AudioConverter:

	def __init__(self, path):
		self.path = path

	def convert_to_audio(self):
		'''
		Converts video file to mp3.
		Uses parameter of path: full path to video file.
		ex: users\\directory\\poop.mkv

		Parameters:
	    None

	    Returns:
	    list of files converted to mp3: ex - ['file1.mp3', 'file2.mp3']

		'''
		clip = mp.VideoFileClip(self.path)

		new_name = os.path.splitext(self.path)[0] + ".mp3"
		clip.audio.write_audiofile(new_name)

		#close file
		del clip.reader
		del clip

		return new_name

def convert_all(path):
	'''
	Converts all video files in given directory to mp3.

	Parameters:
    path (str): directory of files to be converted

    Returns:
    list of files converted to mp3: ex - ['file1.mp3', 'file2.mp3']

	'''
	extensions = {".mp4", ".wmv", ".avi", ".webm", ".mkv", ".flv"}
	files_converted = []

	for file in os.listdir(path):
		for filetype in extensions:
			if file.endswith(filetype):
				mp3_file = file.split(filetype)[0] + ".mp3"
				print("Converting: ", mp3_file)
				video_to_convert = AudioConverter(path + "\\" + file)
				video_to_convert.convert_to_audio()
				files_converted.append(mp3_file)

	return files_converted