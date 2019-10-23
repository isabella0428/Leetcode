class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return []
        nums.sort()
        distance = float('inf')
        final_sum = None

        for i in range(len(nums) -2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                new = nums[i] + nums[r] + nums[l]
                if abs(new - target) < distance:
                    distance = abs(new - target)
                    final_sum = new
                if new < target:
                    l = l + 1
                elif new == target:
                    return final_sum
                else:
                    r = r - 1
        return final_sum


if __name__ == "__main__":
    a = Solution()
    print(a.threeSumClosest(
[1,1,-1,-1,3], -1))



