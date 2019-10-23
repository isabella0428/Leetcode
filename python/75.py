class Solution:
    # one pass
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        k = len(nums)
        for index in range(k):
            v = nums[index]
            nums[index] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1


if __name__ == "__main__":
    a = Solution()
    color = [2,0,2,1,1,0]
    a.sortColors(color)
    print(color)
