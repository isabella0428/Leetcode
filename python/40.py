class Solution1(object):
    def __init__(self):
        self.solution = {}

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(candidates, target, tmp, index):
            if target == 0:
                tmp.sort()
                self.solution[tuple(tmp)] = 1
                return
            if target < min(candidates):
                return
            for j in range(index + 1, len(candidates)):
                tmp.append(candidates[j])
                dfs(candidates, target - candidates[j], tmp[:], j)
                tmp = tmp[:-1]

        candidates.sort()
        for i in range(len(candidates)):
            tmp = []
            tmp.append(candidates[i])
            dfs(candidates, target - candidates[i], tmp, i)
        ret =  list(self.solution.keys())
        for i in range(len(ret)):
            ret[i] = list(ret[i])
        return ret


class Solution2:
    def combinationSum2(self, candidates, target):
        def combine(candidates, path, target):
            nonlocal ret
            if not target:
                path.sort()
                if path not in ret:
                    ret.append(path)
                return
            if not candidates or target < min(candidates) or target < 0:
                return
            for i in range(len(candidates)):
                item = candidates[i]
                if i != 0 and candidates[i] == candidates[i - 1]:
                    continue
                if item <= target:
                    path.append(item)
                    combine(candidates[i + 1:], path[:], target - item)
                    path = path[:-1]

        candidates.sort()
        if candidates[0] > target:
            return []
        ret = []
        combine(candidates, [], target)
        return ret


if __name__ == "__main__":
    a = Solution2()
    print(a.combinationSum2([1, 2], 4))