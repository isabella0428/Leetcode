class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        count = 0
        prev = nums[0]
        index = 0
        while index < len(nums):
            item = nums[index]
            if item != prev:
                prev = item
                count = 1
                index += 1
            else:
                if count >= 2:
                    nums.pop(index)
                else:
                    count += 1
                    index += 1


if __name__ == "__main__":
    a = Solution()
    nums = [0,0,1,1,1,1,2,3,3]
    a.removeDuplicates(nums)
    print(nums)