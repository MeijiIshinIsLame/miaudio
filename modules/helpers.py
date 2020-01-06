from tqdm import tqdm
import os
import time

def convert_to_mins(input_num):
	input_num = int(input_num)
	seconds = (input_num/1000) % 60
	mins = (input_num/(1000*60)) % 60

	full_string = "%d.%02d" % (mins, seconds)

	return full_string

def convert_to_milliseconds(input_str):
	try:
		minsec = input_str.split(":")
		if int(minsec[1]) > 60:
			print("input invalid")
	except Exception as e:
		print(e)
		return -1

	millisec_min = int(minsec[0]) * (60 * 1000) 
	millisec_sec = int(minsec[1]) * 1000
	return millisec_min + millisec_sec

def incriment_pbar(start, end, pbar):
	for i in range(end-start):
		pbar.update(1)

def create_directory_if_none(path):
	if os.path.isdir(path):
		print("\n\nOutput Directory:", path)
	else:
		os.makedirs(path)
		print("\n\nDirectory created: ", os.path.abspath(path))
