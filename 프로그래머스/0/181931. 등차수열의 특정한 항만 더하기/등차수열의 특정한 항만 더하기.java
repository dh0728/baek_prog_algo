class Solution {
    public int solution(int a, int d, boolean[] included) {
        int answer = 0;
        int n  = a;
        if (included[0]) answer += n;
        for(int i = 1; i < included.length; i++){
            n += d;
            if (included[i]) {
                answer += n;
            }
        }
        return answer;
    }
}