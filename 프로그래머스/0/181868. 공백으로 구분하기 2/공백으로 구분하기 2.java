class Solution {
    public String[] solution(String my_string) {
        return my_string.trim().replaceAll("\\s+", " ").split(" ");
        
    }
}