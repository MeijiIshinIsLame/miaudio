def convert_to_mins(input_num):
	input_num = int(input_num)
	seconds = (input_num/1000) % 60
	mins = (input_num/(1000*60)) % 60

	full_string = "%d.%d" % (mins, seconds)

	return full_string

#print(convert_to_mins(46578))

