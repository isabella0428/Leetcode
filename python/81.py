class MySolution:


    pivot = 0
    ans = False
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def findPivot(start, end, nums):
            if start == end:
                return
            mid = (start + end) >> 1
            if nums[mid] < nums[mid - 1]:
                self.pivot = mid
                return
            if nums[mid] > nums[mid + 1]:
                self.pivot = mid + 1
                return
            if nums[mid] > nums[start]:
                return findPivot(mid + 1, end, nums)
            else:
                return findPivot(start, mid - 1, nums)

        def binarySearch(start, end, nums, target):
            if start > end:
                return
            mid = start + end >> 1
            if nums[mid] == target:
                self.ans = True
                return
            if nums[mid] > target:
                return binarySearch(0, mid - 1, nums, target)
            else:
                return binarySearch(mid + 1, end, nums, target)

        def removeDuplicate(nums):
            prev = nums[0]
            if len(nums) == 1:
                return
            i = 1
            while i < len(nums):
                item = nums[i]
                if item == prev:
                    nums.pop(i)
                else:
                    prev = item
                    i += 1
        if not nums:
            return False
        removeDuplicate(nums)
        if nums[len(nums) - 1] <= nums[0]:
            findPivot(0, len(nums) - 1,nums)
            if target == nums[self.pivot]:
                self.ans = True
            elif nums[0] > target > nums[self.pivot]:
                binarySearch(self.pivot + 1, len(nums) - 1, nums, target)
            else:
                binarySearch(0, self.pivot, nums, target)
        else:
            if target == nums[self.pivot]:
                self.ans = True
            elif target > nums[self.pivot]:
                binarySearch(self.pivot + 1, len(nums) - 1, nums, target)
            else:
                binarySearch(0, self.pivot, nums, target)

        return self.ans


class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        mid = l + r >> 1
        while l <= r:
            while l < mid and nums[l] == nums[mid]:
                l += 1
            if nums[mid] == target:
                return True
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            mid = l + r >> 1
        return False


if __name__ == "__main__":
    a = Solution()
    print(a.search([1, 3, 5], 1))
