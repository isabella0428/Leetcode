import java.util.LinkedList;
import java.util.Queue;

class Solution1109 {
    public int[] corpFlightBookings(int[][] bookings, int n) {
        Queue<Integer> queue = new LinkedList<>();
        int[] ret = new int[n];
        for(int i = 0; i <  bookings.length; ++i) {
            while(!queue.isEmpty() && bookings[i][0] > queue.peek())
                queue.remove();
            while(!queue.isEmpty() && bookings[i][0] <= queue.peek() && bookings[i][1] >= queue.peek()) {
                ret[queue.peek()] += booksings[i][2];
                queue.remove();
            }
            for(int i = bookings[i][0]; i <= bookings[i][1]; ++i)
                queue.add(i);
        }
        return ret;
    }
}