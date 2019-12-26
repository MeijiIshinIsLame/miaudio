import moviepy.editor as mp
import os

class AudioConverter:

	def __init__(self, path, ext="mp3"):
		self.path = path
		self.ext = ext

	def convert_to_audio(self):
		clip = mp.VideoFileClip(self.path)

		new_name = os.path.splitext(self.path)[0] + "." + self.ext
		clip.audio.write_audiofile(new_name)

		return new_name

def convert_all(path, ext):
	extensions = {".mp4", ".wmv", ".avi", ".webm", ".mkv"}
	files_converted = []

	for file in os.listdir(path):
		for filetype in extensions:
			if file.endswith(filetype):
				video_to_convert = AudioConverter(path + "\\" + file, ext)
				video_to_convert.convert_to_audio()
				files_converted.append(file)

	return files_converted