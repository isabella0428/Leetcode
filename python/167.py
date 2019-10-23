class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers) - 1
        while start <= end:
            if numbers[start] + numbers[end] < target:
                start += 1
                continue
            if numbers[start] + numbers[end] > target:
                end -= 1
                continue
            return [start + 1, end + 1]


if __name__ == "__main__":
    a = Solution()
    print(a.twoSum([3,24,50,79,88,150,345],
200))