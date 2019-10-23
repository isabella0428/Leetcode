class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def expandAroundElement(index, s):
            left = index - 1
            right = index + 1
            ans = str(s[index])
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    ans = s[left] + ans + s[right]
                    left -= 1
                    right += 1
                else:
                    break
            return ans

        def expandAroundSpace(index, s):
            left = index - 1
            right = index
            ans = ''
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    ans = s[left] + ans + s[right]
                    left -= 1
                    right += 1
                else:
                    break
            return ans

        ans = ''
        for i in range(len(s)):
            center = expandAroundElement(i, s)
            space = expandAroundSpace(i, s)
            if len(center) > len(ans):
                ans = center
            if len(space) > len(ans):
                ans = space
        return ans


if __name__ == "__main__":
    a = Solution()
    print(a.longestPalindrome("babad"))