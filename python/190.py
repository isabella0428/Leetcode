class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret = 0
        for i in range(32):
            ret = ret << 1
            ret |= n & 1
            n = n >> 1
        return ret


if __name__ == "__main__":
    a = Solution()
    print(a.reverseBits(0b00000010100101000001111010011100))