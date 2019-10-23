import unittest


class Solution:
    @staticmethod
    def moveZeroes(nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n, cur = len(nums), 0
        for i in range(n):
            if nums[i] != 0:
                nums[cur] = nums[i]
                cur += 1
        for j in range(cur, n):
            nums[j] = 0
        return nums


class test(unittest.TestCase):
    def testCountZeros(self):
        ans = [[0], [1, 3, 12, 0, 0]]
        input = [[0], [0, 1, 0, 3, 12]]
        for i in range(len(ans)):
            self.assertEqual(ans[i], Solution.moveZeroes(input[i]))


if __name__ == "__main__":
    unittest.main()