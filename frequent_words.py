def frequent_words():
	dna = raw_input("DNA: ")
	k = int(raw_input("k: "))
	counts = {}
	freq_counts = {}
	max_count = 0
	print_str = ''

	for i in range(len(dna) - k):
		str = dna[i:i+k]
		
		if str in counts:
			counts[str] += 1
		else:
			counts[str] = 1

	for j in counts:
		if counts[j] > max_count:
			freq_counts = {j: counts[j]}
			max_count = counts[j]
		elif counts[j] == max_count:
			freq_counts[j] = counts[j]		

	for val in freq_counts:
		print_str += val
		print_str += ' '

	print print_str
	


frequent_words()
