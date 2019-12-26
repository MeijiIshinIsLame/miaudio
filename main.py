import os
from pydub import AudioSegment
import moviepy.editor as mp

import AudioConverter as ac_module
import Splitter as splitter_module
import helpers


if __name__ == "__main__":
	path = ""
	new_path = ""
	ext = "mp3"

	files_list = ac_module.convert_all(path, ext)