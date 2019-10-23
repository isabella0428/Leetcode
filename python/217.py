class Solution1:
    def containsDuplicate(self, nums) -> bool:
        if len(nums) < 2:
            return False
        min_term = min(nums)
        for i in range(len(nums)):
            nums[i] += - min_term
        max_term = max(nums)
        stack = [-1 for i in range(max_term + 1)]
        for item in nums:
            if stack[item] != -1:
                return True
            else:
                stack[item] = item
        return False


class Solution2:
    def containsDuplicate(self, nums) -> bool:
        nums.sort()
        prev = None
        for item in nums:
            if item == prev:
                return True
            prev = item
        return False


if __name__ == "__main__":
    a = Solution2()
    print(a.containsDuplicate([-1200000000,-1200000005]))