class Solution1238 {
    /*
    Problem:    
    Given 2 integers n and start.
    Your task is return any permutation p of (0,1,2.....,2^n -1) such that :p[0] = start
    p[i] and p[i+1] differ by only one bit in their binary representation.
    p[0] and p[2^n -1] must also differ by only one bit in their binary representation.

    Solution:
    Gray code problem.
    First we know that the nth gray code G(n) is i ^(i >> 1)
    XOR with start will not influence the fact that the neighbouring gray codes only have 1 bits different
    start ^ 0 ^ (0  >> 1)   =>  start
    start ^ 1 ^ (1  >> 1)   =>  one bit different with start 
    start ^ 2 ^ (2  >> 1)   =>  one bits different with previous one 
    ..............
    */
    public List<Integer> circularPermutation(int n, int start) {
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < (1 << n); ++i) {
            result.add(start ^ (i) ^ (i >> 1));
        }
        return result;
    }
}