class Solution:
    def hammingDistance(self, x: 'int', y: 'int') -> 'int':
        z, cnt = x ^ y, 0
        while z:
            if z & 1:
                cnt += 1
            z = z >> 1
        return cnt


if __name__ == "__main__":
    a = Solution()
    print(a.hammingDistance(1, 4))