class Solution1:
    # O(n^(0.5))
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        i = 1
        while i * i < x:
            i += 1
        return i - 1

class Solution2:
    # O(nlogn)
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        start, end = 0, int(x - 1)
        ans = 0
        while start <= end:
            medium = (start + end) >> 1
            if medium * medium == x:
                return medium
            if medium * medium > x:
                end = medium - 1
            else:
                start = medium + 1
                ans = medium
        return ans


if __name__ == "__main__":
    a = Solution2()
    print(a.mySqrt(3))

