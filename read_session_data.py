"""Reads in the data for every session and converts it to
an usable object"""

import json
from os import environ, listdir
from os.path import isfile, join

from session import Session
from itribe_time import Time


HOMEDIR = environ['HOME']
FOLDER = HOMEDIR + "/EyeTracking folder/"

def get_files(dirname):
	"""Get all the files in a given directory as a list"""

	files = [f for f in listdir(dirname) if isfile(join(dirname, f))]
	return files

def load_data(filename):
	"""Loads the data from file and returns it as a sequence
	of dicts"""

	with open(filename, "r+") as f:
		data = f.readlines()
		json_data = []
		for point in data:
			json_data.append(json.loads(point))

		return json_data


if __name__ == "__main__":
	#d = load_data(FOLDER + "test.txt")
	#test = Session(d)
	subjects = get_files(FOLDER)
	for subj in subjects[0:1]:
		name = subj.rstrip(".txt")
		itribe_data = load_data(FOLDER + subj)
		sess = Session(itribe_data, Time("adfadf 00:00:26:820"), Time("adfa 00:01:27:520"))
		#sess.print_by_index(10)
		sess_plot = sess.righteye.get_eye_plot()
		sess_plot = sess.lefteye.get_eye_plot()
		sess_plot.savefig(name + ".png")
	#test.print_by_index(0)
	#x = test.righteye.get_eye_plot()
	#x = test.lefteye.get_eye_plot()
	#x.savefig("testplot.png")