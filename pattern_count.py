def patternCount():
	genome = raw_input("Please enter the strand: ")
	pattern = raw_input("Please enter the pattern: ")
	count = 0

	for i in range(len(genome) - len(pattern)):
		if genome[i:].startswith(pattern):
			count += 1
	
	print count

patternCount()
