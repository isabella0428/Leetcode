class Solution:
    def toHex(self, num: 'int') -> 'str':
        map = "0123456789abcdef"
        ans = []
        while num != 0:
            c = map[num & 15]
            ans.insert(0, c)
            num = num >> 4
            if len(ans) == 8:
                break
        return "".join(ans) if ans else "0"
    

if __name__ == "__main__":
    a = Solution()
    print(a.toHex(-1))