import re

class Time:

    def __init__(self, timestr):

        tval = re.split(r"[:]|[.]", timestr.split()[1])

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


if __name__ == "__main__":

    t1 = Time("asfadf 20:20:20:100")
    t2 = Time("asdfas 20:20:20:300")
    t1.abs(t1)
    t2.abs(t1)
    print(t1.lt(t2))
    print(t2.lt(t1))