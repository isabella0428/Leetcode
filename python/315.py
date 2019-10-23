class Solution:
    def countSmaller(self, nums):
        def sort(enum):
            half = int(len(enum) / 2)
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum

        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller


if __name__ == "__main__":
    a = Solution()
    print(a.countSmaller([5,2,6,1]))