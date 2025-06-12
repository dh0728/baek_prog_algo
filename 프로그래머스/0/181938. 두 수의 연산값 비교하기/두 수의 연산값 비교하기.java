class Solution {
    public int solution(int a, int b) {
        int num1 = 2 * a * b;
        String str2 = Integer.toString(a) + Integer.toString(b);
        int num2 = Integer.parseInt(str2);
        
        return num2 >= num1 ? num2 : num1;
    }
}