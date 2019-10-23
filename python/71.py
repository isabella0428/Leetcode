class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        s = path.split('/')
        stack = []
        for item in s:
            if item == '..':
                if stack:
                    stack.pop()
                if stack:
                    stack.pop()
                continue
            if not item or item == '.':
                continue
            stack.append('/')
            stack.append(item)
        if not stack:
            return '/'
        ans = ''
        for i in range(len(stack)):
            ans += stack[i]
        return ans


if __name__ == "__main__":
    a = Solution()
    print(a.simplifyPath("/../"))






