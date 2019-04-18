import matplotlib.pyplot as plt
import time
import re

from itribe_time import Time


def get_frames(data):
    """Not-so-anonymous function to get all datapoints with
    a frame in it"""

    values = [x['values'] for x in data if 'values' in x]
    frames = [x['frame'] for x in values if 'frame' in x]
    return frames


class TrackEye:

    def __init__(self, eye_data):

        self.x = list(map(lambda x: x['raw']['x'], eye_data))
        self.y = list(map(lambda y: y['raw']['y'], eye_data))

    def scale(self, xrange, yrange):

        eye_x = 1960
        eye_y = 1080
        x_r = xrange/eye_x
        y_r = yrange/eye_y
        self.x = [x*x_r for x in self.x]
        self.y = [y*y_r for y in self.y]

    def get_eye_plot(self, plt_):

        plt_.scatter(self.x, self.y, marker=".", alpha=0.5)


class Frame:

    def __init__(self, frame_data, init=None):

        self.time = Time(frame_data["timestamp"])

        if init:
            self.time.abs(init.time)
        
        self.righteye = frame_data['righteye']
        self.lefteye = frame_data['lefteye']

    def print(self):

        print("Time: " + self.time)
        print("Right Eye: " + str(self.righteye))
        print("Left Eye: " + str(self.lefteye))
        print("=======================================")


class Session:

    def __init__(self, json_data, begin="date 00:00:00:000", end="date 60:60:60:100"):
 
        fr = get_frames(json_data)
        init_fr = Frame(fr[0])
        self.frames = [Frame(x, init_fr) for x in fr]

        self.begin_at(begin)
        self.end_at(end)

        reye_dat = [x.righteye for x in self.frames]
        leye_dat = [x.lefteye for x in self.frames]

        self.righteye = TrackEye(reye_dat)
        self.lefteye = TrackEye(leye_dat)

    def print_by_index(self, index):

        self.frames[index].print()

    def begin_at(self, time):
        """Begin at a specific time in the session- i.e: filter out
        all entries before that time"""

        self.frames = [x for x in self.frames if x.time.gt(time)]

    def end_at(self, time):
        """End at at a specific time in the session- i.e: filter out
        all entries after that time"""

        self.frames = [x for x in self.frames if x.time.lt(time)]

