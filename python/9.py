class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        front = []
        reverse = []
        if x < 0:
            return False
        if x < 10:
            return True
        while 1:
            reverse.append(int(x % 10))
            x = int(x / 10)
            if x == 0:
                break

        for i in range(len(reverse)):
            front.append(reverse[len(reverse) - i - 1])

        for i in range(len(reverse)):
            if reverse[i] != front[i]:
                return False

        return True


if __name__ == "__main__":
    a = Solution()
    print(a.isPalindrome(0))