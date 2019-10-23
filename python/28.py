class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):        #start:i
            if haystack[i:i + len(needle)] == needle:           #end:i +len(needle)
                return i
        return -1


if __name__ == "__main__":
    a = Solution()
    print(a.strStr("mississippi",
"issip"))