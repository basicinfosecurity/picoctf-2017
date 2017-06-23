with open(r'hashdump.txt', 'rb') as hashes:
	tmp = {}
	for h in hashes:
		s = h.strip().split(':')
		if s[1] not in tmp.keys():
			tmp[s[1]] = [s[0]]
		else:
			tmp[s[1]].append(s[0])
	for k in tmp.keys():
		print "{}: {}".format(k,len(tmp[k]))
