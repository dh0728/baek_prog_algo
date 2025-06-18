class Solution {
    public int solution(String my_string, String is_prefix) {
        
        int answer = 1;
        
        // 접두사가 더길면
        if(is_prefix.length() > my_string.length()) return 0;
        
        for(int i = 0; i < is_prefix.length(); i++){
            if(is_prefix.charAt(i) != my_string.charAt(i)) {
                answer = 0;
                break;
            }
        }
        
        return answer;
    }
}