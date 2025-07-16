import java.util.Arrays;

class Solution {
    public String[] solution(String myString) {
        return Arrays.stream(myString.split("x"))
                     .filter(s -> !s.isEmpty())  // 빈 문자열 제거
                     .sorted()
                     .toArray(String[]::new);
    }
}
