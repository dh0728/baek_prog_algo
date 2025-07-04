class Solution {
    public int solution(int a, int b, int c) {
        int answer = 0;
        int cnt = countNumber(a, b, c);
        
        // 모두 다르면
        if (cnt == 0) {
            return a + b + c;
        }
        // 두개만 같고 하나 다르면
        if (cnt == 1) {
            return (a + b + c) * (a*a + b*b + c*c);
        }
        // 세 숫자 모두 같으면 
        
        return (a + b + c) * (a*a + b*b + c*c) * (a*a*a + b*b*b + c*c*c);
    }
    
    private int countNumber(int a, int b, int c) {
        int cnt = 0;
        
        if (a == b) {
            cnt +=1;
            if (b == c) {
                cnt +=1;
            }
        } else if (b == c){
            cnt +=1;
        } else if (a == c){
            cnt +=1;
        } 
        return cnt;
    }
}