import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        ArrayList<Integer> list = new ArrayList<>();
        for(int i = 0; i < arr.length; i++) {
            boolean isDelete = false;
            for(int j = 0; j < delete_list.length; j++) {
                if( delete_list[j] == arr[i] ) {
                    isDelete = true;
                    break;
                }    
            }
            if (!isDelete) {
                list.add(arr[i]);
            }
            
        }
        int[] answer = new int[list.size()];
        for(int i = 0; i < answer.length; i++){
            answer[i] = list.get(i);
        }
        return answer;
    }
}