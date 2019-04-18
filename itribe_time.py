import re

class Time:

    def __init__(self, timestr):

        if len(timestr.split()) > 1:
            timestr = timestr.split()[1]

        tval = re.split(r"[:]|[.]", timestr)

        self.h = int(tval[0])
        self.m = int(tval[1])
        self.s = int(tval[2])
        self.ms = int(tval[3])

    def print(self):

        t = str(self.h)  + \
            "-" + str(self.m) + \
             "-" + str(self.s)  + \
             "-" + str(self.ms)
        print(t)

    def sub(self, time):
        """Subtracting the given time from time object"""

        # turning back milliseconds
        if self.ms >= time.ms:
            self.ms -= time.ms
        # else, carry over a minute to subtract
        else:
            self.ms = 1000 - (time.ms - self.ms)
            self.s -= 1

        # turning back seconds
        if self.s >= time.s:
            self.s -= time.s
        # else, carry over a minute to subtract
        else:
            self.s = 60 - (time.s - self.s)
            self.m -= 1
 
        # turning back minutes
        if self.m >= time.m:
            self.m -= time.m
        # else, carry over an hour to subtract
        else:
            self.m = 60 - (time.m - self.m)
            self.h -= 1

        # turning back the hour
        self.h -= time.h


    def add(self, time):
        """Adding the given time from time object"""

        # adding milliseconds
        self.ms += time.ms
        # carry over a second if overflow
        if self.ms > 999:
            self.ms = self.ms - 1000
            self.s += 1

        # adding seconds
        self.s += time.s
        # carry over a minute if overflow
        if self.s > 60:
            self.s = self.s - 60
            self.m += 1
 
        # adding minutes
        self.m += time.m
        # carry over an hour if overflow
        if self.m > 60:
            self.m = self.m - 60
            self.h += 1

        # adding the hours
        self.h += time.h

    def abs(self, init):
        """Absolute time since the beginning of the experiment at init"""

        # turning back milliseconds
        if self.ms >= init.ms:
            self.ms -= init.ms
        # else, carry over a minute to subtract
        else:
            self.ms = 1000 - (init.ms - self.ms)
            self.s -= 1

        # turning back seconds
        if self.s >= init.s:
            self.s -= init.s
        # else, carry over a minute to subtract
        else:
            self.s = 60 - (init.s - self.s)
            self.m -= 1
 
        # turning back minutes
        if self.m >= init.m:
            self.m -= init.m
        # else, carry over an hour to subtract
        else:
            self.m = 60 - (init.m - self.m)
            self.h -= 1

        # turning back the hour
        self.h -= init.h

    def gt(self, time):
        """Greater than comparision"""

        val = False
        if self.h > time.h:
            val = True
        elif self.m > time.m:
            val = True
        elif self.s > time.s:
            val = True
        elif self.ms > time.ms:
            val = True

        return val

    def lt(self, time):
        """Less than comparision"""

        val = False
        if self.h < time.h:
            val = True
        elif self.m < time.m:
            val = True
        elif self.s < time.s:
            val = True
        elif self.ms < time.ms:
            val = True

        return val

    def to_ms(self):
        """Return the absolute value of time in number of ms"""

        ms_ = self.ms
        s_ = self.s * 1000
        m_ = self.m * 1000 * 60
        h_ = self.h * 1000 * 60 * 60
        return ms_ + s_ + m_ + h_

    @staticmethod
    def to_time(value):
        """Convert a Time given in milliseconds to a 
        Time object"""

        new = Time("00:00:00:000")
        new.ms = value % 1000
        value = value // 1000
        new.s = value % 60
        value = value // 60
        new.m = value % 60
        value = value // 60
        new.h = value
        
        return new