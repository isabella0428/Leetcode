import unittest


class Solution:
    @staticmethod
    def canWinNim(n: int) -> bool:
        """
        Determines whether we can win if n stones are left
        :type   n:int
        :rtype  bool
        """
        return not n % 4 == 0


class test(unittest.TestCase):
    def testCanWinNim(self):
        """
        unittest for function canWinNim
        """
        self.assertTrue(Solution.canWinNim(1))
        self.assertFalse(Solution.canWinNim(4))


if __name__ == "__main__":
    unittest.main()