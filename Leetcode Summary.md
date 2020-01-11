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



#### Problems with Tag Array

120. Triangle

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

