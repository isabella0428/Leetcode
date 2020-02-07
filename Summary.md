## Leetcode Summary

References： Leetcode Discussions



#### 最长子序列问题

这种问题的主要思路是采用滑动窗口的方法

滑动窗口：固定窗口的一边，先滑另外一边，再滑这一边



##### 438. Find All Anagrams in a String

找一个字符串a中是字符串b的字母排列组合的子字符串位置

##### 思路：

先固定尾端，移动头端，尾端移到begin～end中包含字符串所有的字符

这时先观察是否满足题目要求的条件（end-begin=b.length() && num == 0）,如果满足就可以再滑动end

如果不满足，则把begin向左滑动，寻找合适的点，当不包含所有字符串b中的字符时，再次滑动end

```java
class Solution{
    public List<Integer> findAnagrams(String s, String p) {
      // s: source string	p:target string
      // Find all anagrams of p in s
      
      // Extreme conditions
    	if(p.length() > s.length()) {
        return new ArrayList<>();
      }
      
      List<Integer> res = new ArrayList<>();
      Map<Character, Integer> map = new HashMap<>();
      
      // Caculate each character's appearance numbers
      for(char c : p.toCharArray()) {
        map.put(c, map.getOrDefault(c, 0) + 1);
      }
      
      // Two partition points of sliding window
      int begin = 0, end = 0;
      int count = map.size();				
      while(end < s.length()) {
        // Move end to right
        char t = s.charAt(end);
        if(map.containsKey(t)) {
          map.put(t, map.get(t) - 1);
          if(map.get(t) == 0) {
            count--;
          }
        }
        end++;
        
        while(count == 0) {
          // Check if begin is the right answer
          if(end - begin == p.length()) {
            res.add(begin);
            break;
          }
          
          // Move begin to right
          char k = s.charAt(begin);
          if(map.containsKey(k)) {
            map.put(k, map.get(k) + 1);
            if(map.get(k) > 0)
              count ++;
          }
          begin++;
        }  
      }
      return res;
    }
}
```



##### 例题：3. Longest Substring Without Repeating Characters

找一个字符串a中最长的不重复子序列长度

##### 思路：

这题的思路比较直接，和上面一题也比较相似，利用Set保存出现过的字符

每次把begin向右移一位

把end滑到最右边（直到下一个字符重复），选取最大的长度

```java
import java.util.*;

class Solution3 {
    public int lengthOfLongestSubstring(String s) {
        if(s.equals(""))
            return 0;
        
        int begin = 0, end = 0;
        HashSet<Character> set = new HashSet<>();
        int maxL = 1;
        
        while(begin < s.length() - 1) {
            while(end < s.length()) {
                char c = s.charAt(end);
                if(set.contains(c)) {
                    break;
                 }
                set.add(c);
                end++;
            }
            
            maxL = maxL > end - begin ? maxL : end - begin;
            set.remove(s.charAt(begin));
            begin++;
        }
        return maxL;
    }
}
```



#### 120. Triangle(DP Problems)

给定一个三角形，求从顶端走到最下面的最小路径和（每次只能走相邻的节点）

```java
		 [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
```

##### 思路

观察到这里每两个相邻节点都共享一个branch，这样我们就有了overlapping subproblem

在这里top-down dp会出现一些问题，我们至少需要保存🌲的大小那么大的空间（memorization可以减小空间需求）

在这里bottom-up dp会更好一些

```java
minpath[k][i] = min( minpath[k+1][i], minpath[k+1][i+1]) + triangle[k][i];
```

Or even better, since the row minpath[k+1] would be useless after minpath[k] is computed, we can simply set minpath as a 1D array, and iteratively update itself:

这里从左边开始更新，因为如果从右边开始更新的话，那么minpath[j + 1]已经被更新过，是第i行的数值（需要的是i+1行的数值），minpath[j]是第i+1行的数值，无法进行以下操作

```java
For the kth level:
minpath[i] = min( minpath[i], minpath[i+1]) + triangle[k][i]; 
```



##### 1D方法：

```java
import java.util.*;

class Solution120 {
    public int minimumTotal(List<List<Integer>> triangle) {
        int row = triangle.size();
        int dp[] = new int[triangle.get(row - 1).size()];
        
        for(int j = 0; j < triangle.get(row - 1).size(); ++j) {
            dp[j] = triangle.get(row - 1).get(j);
        }
        
        for(int i = row - 2; i >= 0; --i) {
            for(int j = 0; j <= i; ++j) {
                dp[j] = Math.min(dp[j],dp[j + 1]) + triangle.get(i).get(j);
            }
        }
        return dp[0];
    }
}
```



#### 870. Advantage Shuffle

找到一个A的permutation，使得A[i] > B[i]的个数最多（A和B长度相等）

##### 思路：

由于选取刚刚超过B[i]的A[i]可以让A beat B的个数更有可能更多，因此这里其实是个Greedy问题。在每一步，我们都选取正好大于B[i]的A中元素与之对应

##### 细节考虑：

1. 由于在B中可能有相同元素，因此我们不能直接简单的保存一个Map<Integer, Integer>，后面的Key会覆盖前面的Key（这里可以使用Deque，FIFO）
2. 在找对应元素的时候，应该遍历A，寻找正好大于B中元素的值，否则要判断边界
3. 在复制数组的时候需要考虑是浅拷贝（没有创建新的对象，=）还是深拷贝（创建新的对象，clone）



```java
import java.util.*;

class Solution870 {
	public int[] advantageCount(int[] A, int[] B) {
		int[] sortedA = A.clone();
    Arrays.sort(sortedA);
    int[] sortedB = B.clone();
    Arrays.sort(sortedB);
    
    // Stores the sortedB's corresponding sortedA values
    Map<Integer, Deque<Integer>> map = new HashMap<>();
    // Stores the remaining sortedA values
    Deque<Integer> remaining = new LinkedList<>();
    
    for(int b: sortedB)
    	map.put(b, new LinkedList());
      
    int b = 0;	// index of which we have beated
    for(int a : sortedA) {
      if(a > sortedB[b]) {
        map.get(sortedB[b++]).add(a);
      } else {
        remaining.add(a);
      }
    }
    
    int[] res = new int[A.length];
    for(int i = 0; i < A.length; ++i) {
      if(map.get(B[i]).size() != 0) {
        res[i] = map.get(B[i]).pop();
      } else {
        res[i] = remaining.pop();
      }
    }
    return res;
	}
}
```



#### 542. 01Matrix(BFS, DP)

给定一个0，1矩阵，找到每个格子离最近的0的距离，返回与原矩阵等大的距离矩阵

这里的距离指的是上下左右，不包括斜对角

##### 思路：

我首先的思路是利用BFS，把0的位置距离设为0，然后把临近的点加入队列，之后重复

这里的一个小优化是把还没计算过距离的点的距离设为Integer.MAX_VALUE，这样就可以避免使用一个visited矩阵来记录是否计算过这个点。

```java
import java.util.*;

// BFS
class Solution542 {
    public int[][] updateMatrix(int[][] matrix) {
        Deque<List<Integer>> cells = new LinkedList<>();
        int[][] dist = new int[matrix.length][matrix[0].length];
        int row = matrix.length, col = matrix[0].length;

        int steps = 0;
        for (int i = 0; i < row; ++i) {
            for (int j = 0; j < col; ++j) {
                if (matrix[i][j] == 0) {
                    List<Integer> l = Arrays.asList(i, j);
                    cells.add(l);
                }
                else {
                    dist[i][j] = Integer.MAX_VALUE;
                }
            }
        }

        steps++;
        while (!cells.isEmpty()) {
            Deque<List<Integer>> temp = new LinkedList<>();
            while (cells.size() != 0) {
                List<Integer> l = cells.pop();
                int r = l.get(0), c = l.get(1);

                // Test if its up, down, left, right neighbour have been visited
                if (testVisited(r + 1, c, row, col, dist)) {
                    dist[r + 1][c] = steps;
                    temp.add(Arrays.asList(r + 1, c));
                }

                if (testVisited(r - 1, c, row, col, dist)) {
                    dist[r - 1][c] = steps;
                    temp.add(Arrays.asList(r - 1, c));
                }

                if (testVisited(r, c + 1, row, col, dist)) {
                    dist[r][c + 1] = steps;
                    temp.add(Arrays.asList(r, c + 1));
                }

                if (testVisited(r, c - 1, row, col, dist)) {
                    dist[r][c - 1] = steps;
                    temp.add(Arrays.asList(r, c - 1));
                }
            }
            cells = temp;
            steps++;
        }
        return dist;
    }

    private boolean testVisited(int i, int j, int row, int col, int[][] dist) {
        if (i < 0 || i >= row || j < 0 || j >= col || dist[i][j] != Integer.MAX_VALUE)
            return false;
        return true;
    }
}
```



#### DP做法

只要知道了附近点到0的距离，就可以计算出当前点到0的距离，这就是个DP问题

当时没想到怎么做是因为四个方向不知道怎么划分子问题

在这里看到答案里面进行了two pass，第一次先根据左边和下面的点计算当前点

第二次根据右边的点和上面的点计算当前点

```java
import java.util.*;

class Solution {
    public int[][] updateMatrix(int[][] matrix) {
        int row = matrix.length, col = matrix[0].length;
        int [][]dp = new int[row][col];
        for(int i = 0; i < row; ++i) {
            for(int j = 0; j < col; ++j) {
                dp[i][j] = Integer.MAX_VALUE - 100000;
            }
        }
        
        for(int i = 0; i < row; ++i) {
            for(int j = 0; j < col; ++j) {
                if(matrix[i][j] == 0) {
                   dp[i][j] = 0;
                }
                else {
                    if(i > 0)
                        dp[i][j] = Math.min(dp[i][j], dp[i - 1][j] + 1);
                    if(j > 0)
                        dp[i][j] = Math.min(dp[i][j], dp[i][j - 1] + 1);
                }
            }
        }
        
        for(int i = row - 1; i >= 0; --i) {
            for(int j = col - 1; j >= 0; --j) {
                if(i < row - 1)
                        dp[i][j] = Math.min(dp[i][j], dp[i + 1][j] + 1);
                    if(j < col - 1)
                        dp[i][j] = Math.min(dp[i][j], dp[i][j + 1] + 1);
            }
        }
        return dp;
    }
}
```

