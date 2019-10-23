class Solution:
    def countPrimes(self, n: 'int') -> 'int':
        tmp = [True for i in range(n + 1)]
        if n < 3:
            return 0
        count = 0
        for i in range(3, n + 1):
            if tmp[i - 1]:
                count += 1
                # avoid counting repeatedly eg: 2 * 3 and 3 * 2
                for j in range((i - 1) ** 2, n, i - 1):
                    tmp[j] = False
        return count


if __name__ == "__main__":
     a = Solution()
     print(a.countPrimes(10))
