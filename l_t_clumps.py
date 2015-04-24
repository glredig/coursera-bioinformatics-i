def l_t_clumps():
	filename = raw_input("Filename: ")
	k = int(raw_input("k: "))
	l = int(raw_input("l: "))
	t = int(raw_input("t: "))
	genome = ''

	with open(filename) as openFile:
		for line in openFile:
			genome += line.rstrip()

	def print_genome():
		print genome

	print_genome()
	
l_t_clumps()
