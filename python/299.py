class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret = list(secret)
        dicts = {}
        A, B = 0, 0
        for item in secret:
            dicts[item] = dicts.get(item, 0) + 1

        guess = list(guess)
        size = min(len(guess), len(secret))
        B_stack = []
        for i in range(size):
            if guess[i] == secret[i]:
                A += 1
                dicts[guess[i]] -= 1
            else:
                B_stack.append(guess[i])
        for item in B_stack:
            if item in dicts and dicts[item] > 0:
                dicts[item] -= 1
                B += 1
        return "{}A{}B".format(A, B)


if __name__ == "__main__":
    a = Solution()
    print(a.getHint("1122", "1222"))