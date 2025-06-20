class Solution {
    public String solution(String my_string, int n) {
        int string_len = my_string.length();
        String answer = my_string.substring(string_len - n);
        return answer;
    }
}