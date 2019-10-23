import static java.util.stream.Collectors.toList;

class Solution {
    Map<String, List<String>> numberCharMap;
    List<String> output = new ArrayList<>();

    public List<String> letterCombinations(String digits) {
        if (digits.equals(""))
            return output;
        setMap();
        letterCombinations(digits, 0, "");
        return output;
    }

    public void letterCombinations(String digits, int loc, String temp) {
        if (loc == digits.length()) {
            output.add(temp);
            return;
        }

        List<String> valList = numberCharMap.get(String.valueOf(digits.charAt(loc)));

        String next_temp = "";
        for (String s : valList) {
            next_temp = temp + s;
            letterCombinations(digits, loc + 1, next_temp);
        }
    }

    public void setMap() {
        numberCharMap = new HashMap<>();
        numberCharMap.put("2", Stream.of("a", "b", "c").collect(toList()));
        numberCharMap.put("3", Stream.of("d", "e", "f").collect(toList()));
        numberCharMap.put("4", Stream.of("g", "h", "i").collect(toList()));
        numberCharMap.put("5", Stream.of("j", "k", "l").collect(toList()));
        numberCharMap.put("6", Stream.of("m", "n", "o").collect(toList()));
        numberCharMap.put("7", Stream.of("p", "q", "r", "s").collect(toList()));
        numberCharMap.put("8", Stream.of("t", "u", "v").collect(toList()));
        numberCharMap.put("9", Stream.of("w", "x", "y", "z").collect(toList()));
    }
}