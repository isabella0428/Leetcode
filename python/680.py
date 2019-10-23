class Solution:
    #greedy
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPali(s, i, j):
            return all(s[k] == s[j - k + i] for k in range(i, j))

        for i in range(len(s)):
            if s[i] != s[~i]:       # ~i = -(i + 1)
                j = len(s) - 1 - i
                return isPali(s, i + 1, j) or isPali(s, i, j - 1)
        return True


if __name__ == "__main__":
    a = Solution()
    print(a.validPalindrome('abc'))