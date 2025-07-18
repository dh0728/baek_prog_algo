import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr, boolean[] flag) {
        ArrayList<Integer> list = new ArrayList<>();
        for(int i = 0; i < arr.length; i++) {
            if (flag[i]) {
                for(int x = 0; x < arr[i]*2; x++){
                    list.add(arr[i]);
                }
            } else {
                int n = list.size() - 1;
                for(int x = n; x > n - arr[i]; x--) {
                    list.remove(x);
                }
            }
        }
        
        int[] answer = new int[list.size()];
        
        for(int i =0; i < list.size(); i++){
            answer[i] = list.get(i);
        }
            
        return answer;
    }
}