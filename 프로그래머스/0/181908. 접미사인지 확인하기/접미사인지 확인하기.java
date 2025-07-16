class Solution {
    public int solution(String my_string, String is_suffix) {
        if (my_string.contains(is_suffix)) { //일단 일치하는게 있으면
            int x = my_string.length() - 1;
            for(int i = is_suffix.length() - 1; i >= 0; i--){
                if(my_string.charAt(x) != is_suffix.charAt(i)) {
                    return 0;
                }
                x--;
            }
            return 1;
            
        } else {
            return 0;
        }
    }
}