class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        size = len(nums)
        if size == 1:
            return nums[0]
        if nums[-1] > nums[0]:          # following algorithm only
            return nums[0]              # fit for rotated  array
        while left <= right:
            mid = int((left + right) >> 1)
            val = nums[mid]
            if nums[mid] <= nums[mid - 1]:
                return nums[mid]
            if nums[mid + 1] <= nums[mid]:
                return nums[mid + 1]
            if nums[mid] > nums[left]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid - 1


if __name__ == "__main__":
    a = Solution()
    print(a.findMin([1, 2, 3]))