class Solution1232 {
    public boolean checkStraightLine(int[][] coordinates) {
        if (coordinates[1][0] - coordinates[0][0] == 0) {
            for (int i = 2; i < coordinates.length; ++i) {
                if (coordinates[i][0] != coordinates[0][0])
                    return false;
            }
            return true;
        }
        
        if (coordinates[1][1] - coordinates[0][1] == 0) {
            for (int i = 2; i < coordinates.length; ++i) {
                if (coordinates[i][1] != coordinates[0][1])
                    return false;
            }
            return true;
        }
            
        double linear = (coordinates[1][0] - coordinates[0][0]) / (coordinates[1][1] - coordinates[0][1]);
        for (int i = 2; i < coordinates.length; ++i) {
            if(coordinates[i][1] - coordinates[i - 1][1] == 0)
                return false;
            if ((coordinates[i][0] - coordinates[i - 1][0]) / (coordinates[i][1] - coordinates[i - 1][1]) != linear)
                return false;
        }
        return true;
    }
}