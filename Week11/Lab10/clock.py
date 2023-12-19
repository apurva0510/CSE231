class Time:
    def __init__(self, hour=0, minute=0, second=0):
        """ Construct a Time using three integers. """
        self.hour = hour
        self.minute = minute 
        self.second = second

    def __repr__(self):
        """ Return a string with the format “Class Time: hh:mm:ss” """
        return "Class Time: {:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

    def __str__(self):
        """ Return a string with the format “hh:mm:ss” """
        return "{:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

    def from_str(self, time_str):
        """ Convert a string (hh:mm:ss) into a Time. """
        hour, minute, second = [int(n) for n in time_str.split(':')]
        self.hour = hour
        self.minute = minute
        self.second = second

    def add_times(self, other):
        """ Add two Time objects and return a Time object. """
        hour = self.hour + other.hour
        minute = self.minute + other.minute
        second = self.second + other.second

        if second >= 60:
            second -= 60
            minute += 1

        if minute >= 60:
            minute -= 60
            hour += 1

        if hour >= 24:
            hour -= 24

        return Time(hour, minute, second)

    def sub_times(self, other):
        """ Subtract two Time objects and return a Time object. """
        hour = self.hour - other.hour
        minute = self.minute - other.minute
        second = self.second - other.second

        if second < 0:
            second += 60
            minute -= 1

        if minute < 0:
            minute += 60
            hour -= 1

        if hour < 0:
            hour += 24

        return Time(hour, minute, second)