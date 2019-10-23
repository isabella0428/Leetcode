class Solution:
    # get the overlap region area
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        overlap = max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0)
        return (A - C) * (B - D) + (E - G) * (F - H) - overlap


if __name__ == "__main__":
    a = Solution()
    print(a.computeArea(-3,0,3,4,0,-1,9,2))