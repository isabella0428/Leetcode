import java.util.*;

class Solution1233 {
    public static void main(String ... args) {
        String[] folder = {"/a","/a/b/c","/a/b/d"};
        System.out.println(removeSubfolders(folder));
    }

    public static List<String> removeSubfolders(String[] folder) {
        List<String> result = new ArrayList<>();
        Arrays.sort(folder, Comparator.comparing(s -> s.length()));

        for(String s : folder) {
            int is_subfolder = 0;
            for (int i = 0; i < s.length(); ++i) {
                if (s.charAt(i) == '/' && result.contains(s.substring(0, i)))
                {
                    is_subfolder = 1;
                    break;
                }
            }
            if (is_subfolder == 0)
                result.add(s);
        }
        return result;
    }
}