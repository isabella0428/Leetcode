class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlap = []

    def book(self, start: int, end: int) -> bool:
        for i, j in self.overlap:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlap.append([max(i, start), min(end, j)])
        self.calendar.append([start, end])
        return True


if __name__ == "__main__":
    a = MyCalendarTwo()
    print(a.book(10, 20))
    print(a.book(50, 60))
    print(a.book(10, 40))
    print(a.book(5, 15))
    print(a.book(5, 10))
    print(a.book(25, 55))
