"""Reads in the data for every session and converts it to
an usable object"""

import json
from os import environ, listdir, mkdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import copy


from session import Session
from itribe_time import Time
from image_manip import stack_graphs, put_image


HOMEDIR = environ['HOME']
FOLDER = HOMEDIR + "/EyeTracking folder/"
START_STOP = "start_stop.txt"


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


def load_start_stop(filename):
	"""Load manually-recorded start and stop times for every participant"""

	with open(filename, "r+") as f:
		s = f.readlines()
		data = {}

		for i in s:
			temp = i.split()
			name = temp[0]
			start = Time(temp[1])
			stop = Time(temp[2])
			data[name] =  (start, stop)

		return data


if __name__ == "__main__":

	subjects = get_files(FOLDER)
	times = load_start_stop(START_STOP)

	try:
		mkdir("plots")
	except FileExistsError:
		pass

	for subj in subjects:

		# get name, data for session
		name = subj.rstrip(".txt")
		itribe_data = load_data(FOLDER + subj)

		# get start/stop time for session
		start = times[name][0]
		stop = times[name][1]

		# get the absolute runtime of the session, and
		# divide by 12 (number of sentences), and then
		# get the Time-format runtime of every sentence
		# from this
		stop.sub(start)
		per_s = stop.to_ms() // 12
		per_s = Time.to_time(per_s)

		# make a list of 12 Session objects for the given data
		# one for every sentence
		sent_tracks = []
		plots = []
		for i in range(12):

			end = copy.deepcopy(start)
			end.add(per_s)

			sess = Session(itribe_data, start, end)
			sent_tracks.append(sess)

			# increment start value
			start.add(per_s)
		
			# initialize matplotlib figure
			fig = plt.figure()
			ax = fig.add_subplot(111)
			#ax.set_ylim(bottom=1000, top=0)
			# put slide image in the plot
			put_image(ax, i + 1)
			xmin, xmax = ax.get_xlim()
			ax.set_xlim(0, xmin + xmax)
			ymin, ymax = ax.get_ylim()
			ax.set_ylim(ymax, ymin)
			ymin, ymax = ax.get_ylim()

			# plot for the current subject and sentence
			ax_ = fig.add_subplot(111)
			sess.righteye.scale(xmax-xmin, ymax-ymin)
			sess.lefteye.scale(xmax-xmin, ymax-ymin)			
			sess.righteye.get_eye_plot(ax_)
			sess.lefteye.get_eye_plot(ax_)
			plotname = "plots/" + name + "_" + str(i) + ".png"
			plt.savefig(plotname)

			plots.append(plotname)
			#plt.show()
			plt.clf()
		# stack all the graphs vertically
		stack_graphs(plots, name + ".png")
	#test.print_by_index(0)
	#x = test.righteye.get_eye_plot()
	#x = test.lefteye.get_eye_plot()
	#x.savefig("testplot.png")
