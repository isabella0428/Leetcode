class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]   #sorted
        :type val: int
        :rtype: int
        """

        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1              # reduce array size by one
            else:
                i += 1
        return n


if __name__ == "__main__":
    a = Solution()
    print(a.removeElement([3, 2, 2, 3], 3))