class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]       #sorted
        :rtype: int
        """
        a, b = 0, 1
        while 1:
            try:
                nums[b]
            except:
                break
            if nums[a] == nums[b]:
                nums.remove(nums[b])
            else:
                a += 1
                b += 1
        return nums


if __name__ == "__main__":
    a = Solution()
    print(a.removeDuplicates([1, 1, 2]))