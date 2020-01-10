## Leetcode Summary

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

