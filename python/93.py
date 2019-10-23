class Solution:
    def restoreIpAddresses(self, s: 'str') -> 'List[str]':
        def dfs(s, path, index):
            if index == 4:
                if not s:
                    possible.append(path[:-1])
                return
            for i in range(1, 4):
                if i <= len(s):
                    if i == 1:
                        dfs(s[i:], path + s[:i] + '.', index + 1)
                    if i == 2 and s[0] != '0':
                        dfs(s[i:], path + s[:i] + '.', index + 1)
                    if i == 3 and s[0] != '0' and int(s[:3]) < 256:
                        dfs(s[i:], path + s[:i] + '.', index + 1)

        possible = []
        dfs(s, "", 0)
        return possible


if __name__ == "__main__":
    a = Solution()
    print(a.restoreIpAddresses("010010"))
