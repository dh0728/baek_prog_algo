class Solution {
    public int[] solution(int[] num_list) {
        int list_len = num_list.length;
        int num = num_list[list_len - 1] - num_list[list_len - 2];
        int[] answer = new int[list_len + 1];
        System.arraycopy(num_list, 0, answer, 0, list_len);
        
        if(num > 0){
            answer[list_len] = num;
        } else {
            answer[list_len] = num_list[list_len -1] * 2;
        }
        
        return answer;
    }
}