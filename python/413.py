class Solution1:
    def numberOfArithmeticSlices(self, A: 'List[int]') -> 'int':
        # dynamic programming
        memo = [0 for i in range(len(A))]
        if len(A) < 3:
            return 0
        sum = 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                memo[i] = memo[i - 1] + 1
                sum += memo[i]
        return sum


class Solution2:
    def numberOfArithmeticSlices(self, A: 'List[int]') -> 'int':
        # dp with constant spaces
        dp = 0
        if len(A) < 3:
            return 0
        sum = 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp += 1
                sum += dp
            else:
                dp = 0
        return sum


if __name__ == "__main__":
    a = Solution2()
    print(a.numberOfArithmeticSlices([1, 2, 3, 4]))
