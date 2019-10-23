class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        count = 0
        end = len(s) - 1
        while s[end] == ' ' and end > -1:
            end -= 1
        for i in range(end, -1, -1):
            if s[i] != ' ':
                count += 1
            else:
                break
        return count

if __name__ == "__main__":
    a = Solution()
    print(a.lengthOfLastWord("a "))