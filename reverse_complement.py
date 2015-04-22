def reverse_complement():
	filename = raw_input("file: ")
	dna_string = ''

	with open(filename) as open_file:
		for line in open_file:
			dna_string += line.rstrip()

	complements = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
	rev_comp = ''

	for ltr in dna_string[::-1]:
		rev_comp += complements[ltr]

	print rev_comp

reverse_complement()
