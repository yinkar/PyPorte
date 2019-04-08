import time
import winsound
import json
import sys



note = {
	"E0": 329,
	"F0": 349,
	"F#0": 369,
	"Gb0": 369,
	"G0": 392,
	"Ab": 415,
	"A": 440,
	"A#": 466,
	"Bb": 466,
	"B": 493,
	"C": 523,
	"C#": 554, 
	"Db": 554,
	"D": 587,
	"D#": 622,
	"Eb": 622,
	"E": 659,
	"F": 698,
	"F#": 739,
	"Gb": 739,
	"G": 783,
	"G#": 830,
	"Ab2": 830,
	"A2": 880,
	"A#2": 932,
	"Bb2": 932,
	"B2": 987,
	"C2": 1046
}

duration = {
	"4": 2000,
	"2": 1000,
	"1.5": 750,
	"1": 500,
	"1/2": 250,
	"1/4": 125,
	"1/8": 63
}



def main():
	if len(sys.argv) != 1: 
		out = sys.argv[1]
	else:
		out = input('Type filename of the json file: ')


	with open(out) as f:
		data = json.load(f)

	composition = data

	'''
	with open('output.json', 'w') as outfile:
		json.dump(composition, outfile)
	'''

	
	animation = "|/-\\"
	idx = 0


	counter = 0

	for i in composition[0]:
		print(animation[idx % len(animation)], end="\r")
		idx = idx + 1

		if i == "-":
			time.sleep(duration[composition[1][counter]]/1000)
		else:
			winsound.Beep(note[i], duration[composition[1][counter]])
		counter = counter + 1



if __name__ == "__main__":
	main()
