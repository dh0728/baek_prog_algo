class Solution {
    public int solution(int a, int b) {
        String strA = Integer.toString(a);
        String strB = Integer.toString(b);
        
        int num1 = Integer.parseInt(strA + strB);
        int num2 = Integer.parseInt(strB + strA);
    
        
        return num1 > num2 ? num1 : num2;
    }
}