"""Reads in the data for every session and converts it to
an usable object"""

import json
import os

HOMEDIR = os.environ['HOME']
FOLDER = HOMEDIR + "/EyeTracking folder/"

def load_data(filename):
	data = f.readlines()
	return data

if __name__ == "__main__":
	print(FOLDER)
	#d = load_data(FOLDER + "test.txt")