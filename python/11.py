class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        sum1 = 0
        i = 0
        j = len(height) - 1
        while i < j:
            if height[i] < height[j]:
                lower = i
                new = height[lower] * (j - i)
                i = i + 1
            else:
                lower = j
                new = height[lower] * (j - i)
                j = j - 1

            if new > sum1:
                sum1 = new

        return sum1



if __name__ == "__main__":
    a = Solution()
    print(a.maxArea([1,8,6,2,5,4,8,3,7]))