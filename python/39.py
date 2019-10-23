class Solution1(object):
    def __init__(self):
        self.solution = {}

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def Permutation(depth, candidates, target, tmp):
            if target == 0:
                tmp.sort()
                self.solution[tuple(tmp)] = 1
                return
            if target < min(candidates):
                return
            for j in range(len(candidates)):
                if candidates[j] > min(candidates):
                    return
                tmp.append(candidates[j])
                Permutation(j, candidates, target - candidates[j], tmp.copy())
                tmp = tmp[:-1]

        candidates.sort()
        min_term = candidates[0]
        tmp = []
        if target < min_term:
            return []
        for i in range(len(candidates)):
            tmp.append(candidates[i])
            Permutation(i + 1, candidates, target - candidates[i], tmp)
            tmp = []

        ret = list(self.solution.keys())
        for i in range(len(ret)):
            ret[i] = list(ret[i])
        ret.sort()
        return ret


class Solution2:
    def combinationSum(self, candidates, target):
        if target < min(candidates):
            return []
        dp = [[] for i in range(target + 1)]
        candidates.sort()
        for item in candidates:
            if item <= target:
                dp[item].append([item])
        for i in range(1, target + 1):
            for item in candidates:
                if i <= item:
                    break
                if i > item and dp[i - item]:
                    for a in dp[i - item]:
                        tmp = a[:]
                        tmp.append(item)
                        tmp.sort()
                        if tmp not in dp[i]:
                            dp[i].append(tmp)
                    dp[i].sort()
        return dp[target]


if __name__ == "__main__":
    a = Solution2()
    print(a.combinationSum([8,7,4,3],
11))