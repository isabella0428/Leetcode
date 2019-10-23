class Solution1:
    def canJump(self, nums):                #backtracking
        """
        :type nums: List[int]
        :rtype: bool
        """

        def Jump(nums, index):
            if index == len(nums) - 1:
                return True
            if nums[index] == 0:
                return
            for i in range(nums[index] + 1, 0, -1):
                if Jump(nums, index + 1):
                    return True
            return False
        return Jump(nums, 0)


class Solution2:
    # dynamic programming top-down
    def __init__(self):
        self.memo = []

    Good = 0
    Bad = 1
    Unknown = 2

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def jumpFromPosition(loc, nums):
            if self.memo[loc] != self.Unknown:
                return self.memo[loc] == self.Good
            furthest_jump = min(loc + nums[loc], len(nums) - 1)
            for jump in range(loc + 1, furthest_jump + 1):
                if jumpFromPosition(jump, nums):
                    self.memo[loc] = self.Good
                    return True
            self.memo[loc] = self.Bad
            return False

        self.memo = [self.Unknown for i in range(len(nums))]
        self.memo[-1] = self.Good
        return jumpFromPosition(0, nums)


class Solution3:
    # dynamic programming bottom up
    # aimed at eliminating recursion

    def __init__(self):
        self.memo = []
    Good = 0
    Bad = 1
    Unknown = 2

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.memo = [self.Unknown for i in range(len(nums))]
        self.memo[-1] = self.Good
        for i in range(len(nums) - 2, -1, -1):
            furthest_jump = min(nums[i] + i, len(nums) - 1)
            for j in range(i + 1, furthest_jump + 1):
                if self.memo[j] == self.Good:
                    self.memo[i] = self.Good
                    break
        return self.memo[0] == self.Good


class Solution4:
    # check if we can reach the left-most good index
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        left_most = len(nums) - 1
        for i in range(left_most - 1, -1, -1):
            if i + nums[i] >= left_most:
                left_most = i
        return left_most == 0







if __name__ == "__main__":
    a = Solution4()
    print(a.canJump([1,1,1]))