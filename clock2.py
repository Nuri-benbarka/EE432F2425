class Clock:
    def __init__(self,hour=0,minutues=0,seconds=0):
        if 0 <= hour <= 23 and 0 <= minutues <= 59 and 0 <= seconds <= 59:
            self._hr = hour
            self._min = minutues
            self._sec = seconds
        else:
            raise ValueError("invalid clock values")

    def __str__(self):
        return f"{self._hr}:{self._min}:{self._sec}"

    def tic(self):
        self._sec += 1
        if self._sec >= 60:
            self._sec = 0
            self._min += 1
            if self._min >= 60:
                self._min = 0
                self._hr += 1
                self._hr %= 24

    def settime(self,hour=0,minutues=0,seconds=0):
        self._hr = hour
        self._min = minutues
        self._sec = seconds

    def __sub__(self, other):
        result = 0
        result += self._sec - other._sec
        result += (self._min - other._min) * 60
        result += (self._hr - other._hr) * 3600
        return result

if __name__ == "__main__":
    try:
        myclock = Clock(100)
    except ValueError:
        myclock = Clock()
    another_clock = Clock(12,30)

    #another_clock._hr = 50

    print(myclock)
    print(another_clock._hr)

    myclock.settime(23,59,59)
    myclock.tic()
    print(myclock)
    print(myclock-another_clock)
    print(another_clock - myclock)