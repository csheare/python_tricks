# Idiom 1: Use a context manager to ensure resources are properly managed - WOW MAN

with open(path_to_file, 'r') as file_handle:
	for line in file_handle:
		if raise_exception(line):
			print('No! An Exception!')