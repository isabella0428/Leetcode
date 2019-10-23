class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        char = []
        num = 0
        longest = 0
        for i in s:
            if i not in char:
                char.append(i)
                num = num + 1
                if longest < num :
                    longest = num
            else:
                longest = num if num > longest else longest
                loc = char.index(i)
                char = char[loc + 1:]
                char.append(i)
                num = num - loc
        return longest


if __name__ == "__main__":
    a = Solution()
    print(a.lengthOfLongestSubstring("au"))