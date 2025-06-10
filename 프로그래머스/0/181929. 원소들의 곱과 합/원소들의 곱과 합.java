class Solution {
    public int solution(int[] num_list) {
        int list_len = num_list.length;
        int numSum = 0;
        int numMult = 1;
        for(int i = 0; i < list_len ; i++){
            numSum += num_list[i];
            numMult *= num_list[i];
        }
        if (numSum*numSum > numMult) {
            return 1;
        } else {
            return 0;
        }
    }
}