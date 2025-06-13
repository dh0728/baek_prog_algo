class Solution {
    public int solution(int[] num_list) {
        String oddNum = "";
        String evenNum ="";
        
        for (int i = 0; i < num_list.length; i++){
            if (num_list[i] % 2 == 1) { //홀수
                oddNum += Integer.toString(num_list[i]);
            } else{
                evenNum += Integer.toString(num_list[i]);
            }
        }
        int answer = Integer.parseInt(oddNum) + Integer.parseInt(evenNum);
        
        return answer;
    }
}