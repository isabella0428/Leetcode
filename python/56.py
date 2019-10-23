class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution1:
    def __init__(self):
        self.result = []

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        def overlap(list1, list2):
            return list1.end >= list2.start and list1.start <= list2.end

        if not intervals:
            return []
        self.result = [intervals[0]]
        for i in range(1, len(intervals)):
            for j in range(len(self.result)):
                if overlap(intervals[i], self.result[j]):
                    self.result[j] = Interval(min(intervals[i].start,self.result[j].start), max(intervals[i].end, self.result[j].end))
                else:
                    if intervals[i] not in self.result:
                        self.result.append(intervals[i])
        for i in range(len(self.result)):
            for j in range(i, len(self.result)):
                if i >= len(self.result) or j >= len(self.result):
                    break
                if overlap(self.result[i], self.result[j]):
                    self.result[i] = Interval(min(self.result[i].start, self.result[j].start), max(self.result[i].end, self.result[j].end))
                    self.result.pop(j)

        return self.result


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution2:
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.end)
        result = [intervals[0]]
        for item in intervals[1:]:
            if item.start > result[-1].end:
                result.append(item)
            else:

                n = len(result) - 1
                while n >= 0 and result[n].start > item.start:
                    result.pop()
                    n -= 1
                if not result or result[-1].end < item.start:
                    result.append(item)
                else:
                    result[-1].end = item.end
        return result



if __name__ == "__main__":
    a = Solution2()
    intervals = [Interval(3,3), Interval(3,5), Interval(1,3),Interval(2,4),Interval(0,0),Interval(4,6),Interval(2,2),Interval(1,2),Interval(3,3),Interval(3,4)]
    for item in a.merge(intervals):
        print(item.start, item.end)
