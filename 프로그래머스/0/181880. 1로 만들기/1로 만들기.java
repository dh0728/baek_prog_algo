class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        for(int n : num_list){
            int i = 0;
            while(n != 1){
                if (n % 2 == 1){
                    n = (n -1) / 2;
                } else {
                    n = n / 2;
                }
                i++;
            }
            answer += i;
        }
        return answer;
    }
}