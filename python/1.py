class Solution1:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        O(n^2)
        """

        for i in range(len(nums)):
            a = nums[i]
            for j in range(i + 1, len(nums)):
                b = nums[j]
                if a + b == target:
                    return [i, j]


class Solution2:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        O(n)
        """

        dict = {}
        for i in range(len(nums)):
            if str(nums[i]) not in dict:
                dict[str(nums[i])] = i
        for i in range(len(nums)):
            if str(target - nums[i]) in dict and dict[str(target - nums[i])] != i:
                return [i, dict[str(target - nums[i])]]


class Solution3:
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        O(n)
        """

        dict = {}
        for i in range(len(nums)):
            if str(nums[i]) not in dict:
                dict[str(nums[i])] = i
            if str(target - nums[i]) in dict and dict[str(target - nums[i])] != i:
                return [dict[str(target - nums[i])], i]


if __name__ == "__main__":
    a = Solution3()
    print(a.twoSum([2, 3], 5))

test branch