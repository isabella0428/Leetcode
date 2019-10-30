import java.util.*;

class Solution1217 {
    /* Problem: 1217. Play with Chips
    There are some chips, and the i-th chip is at position chips[i].    
    You can perform any of the two following types of moves any number of times (possibly zero) on any chip:

    Move the i-th chip by 2 units to the left or to the right with a cost of 0.
    Move the i-th chip by 1 unit to the left or to the right with a cost of 1.
    There can be two or more chips at the same position initially.

    Return the minimum cost needed to move all the chips to the same position (any position).
    */

        public int minCostToMoveChips(int[] chips) {
            int length = chips.length;
            int min_exchanges = Integer.MAX_VALUE;
        for (int i = 0; i < length; ++i) {
            int position = chips[i];
            int changes = 0;
            int distance = 0;
        

            for (int c : chips) {
                distance = position - c;
                if (distance < 0)
                    distance = -1 * distance;
                changes += distance % 2;
            }

            min_exchanges = Math.min(changes, min_exchanges);
        }
        return min_exchanges;
    }
}