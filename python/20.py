class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 == 1:
            return False
        stack = []
        mapping = {')': '(', ']': '[', '}': '{' }
        for char in s:
            if char in mapping:
                # assign a dummy value if stack is empty
                top = stack.pop() if stack else '$'

                if top != mapping[char]:
                    return False
                else:
                    continue
            else:
                stack.append(char)
        if not stack:
            return True
        else:
            return False


if __name__ == "__main__":
    a = Solution()
    print(a.isValid("(("))