def pattern_location():
	filename = raw_input("filename: ")
	genome = ''
	with open(filename) as openFile:
		for line in openFile:
			genome += line.rstrip()	
	pattern = raw_input("Pattern: ")
	locations = []
	for i in range(len(genome) - len(pattern)):
		if genome[i:].startswith(pattern):
			locations.append(str(i))

	output_str = ' '.join(locations)

	print output_str

pattern_location()
