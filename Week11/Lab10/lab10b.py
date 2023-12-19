#define your Time class here
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


def main():
    A = Time( 12, 25, 30 )

    print(A)
    print(repr(A))
    print(str(A))
    print()

    B = Time(2, 25, 3)

    print(B)
    print(repr(B))
    print(str(B))
    print()

    C = Time(2, 25)

    print(C)
    print(repr(C))
    print(str(C))
    print()

    D = Time()

    print(D)
    print(repr(D))
    print(str(D))
    print()

    D.from_str("03:09:19")

    print(D)
    print(repr(D))
    print(str(D))


if __name__ == "__main__":
    main()
