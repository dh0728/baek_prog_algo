class Solution {
    public String solution(String n_str) {
        String answer = "";
        
        int i = 0;
        while(n_str.charAt(i) == '0') {
            i += 1;
        }
        answer = n_str.substring(i);
        return answer;
    }
}