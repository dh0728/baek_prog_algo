class Solution {
    public String solution(String my_string, int[] indices) {
        int[] is_string = new int[my_string.length()];
        String answer = "";
        for(int i = 0; i < indices.length; i++){
            is_string[indices[i]] = 1;
        }
        
        for(int i = 0; i < my_string.length(); i++){
            if( is_string[i] == 0) {
                answer += my_string.charAt(i);
            }
        }
        
        
        return answer;
    }
}