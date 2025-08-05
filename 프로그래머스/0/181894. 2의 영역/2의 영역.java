class Solution {
    public int[] solution(int[] arr) {
        int[] two_idx = {-1,-1};
        
        for(int i =0; i < arr.length; i++){
            if(arr[i] == 2){
                if (two_idx[0] == -1){
                    two_idx[0] = i;
                } else{
                    two_idx[1] = i;
                }
            }    
        }
        if( two_idx[0] == -1) {
            int[] answer = {-1};
            return answer;
        } else {
            if (two_idx[1] == -1) {
                int[] answer = {2};
                return answer;
            } else {
                int[] answer = new int[two_idx[1] - two_idx[0] + 1];
                for(int i = two_idx[0]; i <= two_idx[1]; i++) {
                    answer[i -two_idx[0]] = arr[i];
                }
                return answer;
            }
        }
        
    }
}