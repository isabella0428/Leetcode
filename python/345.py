class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        l = 0
        r = len(s) - 1
        vowels = 'AEIOUaeiou'
        while l < r:
            while s[l] not in vowels and l < r:
                l += 1
            while s[r] not in vowels and l < r:
                r -= 1
            if l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return "".join(s)


if __name__ == "__main__":
    a = Solution()
    print(a.reverseVowels(".,"))