def checkAnagram(input):
	dict = {}
	for strVal in input:
		key = ''.join(sorted(strVal))
		if key in dict.keys():
			dict[key].append(strVal)
		else:
			dict[key] = []
			dict[key].append(strVal)
	output = ""
	for key,value in dict.items():
		output = output + ' '.join(value) + ' '
	return output
if __name__ == "__main__":
	input=['low', 'race', 'care', 'owl']
	print (checkAnagram(input))

