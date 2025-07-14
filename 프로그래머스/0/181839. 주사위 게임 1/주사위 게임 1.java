class Solution {
    public int solution(int a, int b) {
        int result = a % 2 + b % 2;
        return result == 2 ? a*a + b*b : result == 1 ? 2 * (a + b) : Math.abs(a - b);
    }
}