import java.util.*;

class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        ArrayList<Integer> list = new ArrayList<>();
        
        if(n == 1){
            return Arrays.copyOfRange(num_list, 0, slicer[1] + 1);
        } else if (n == 2) {
            return Arrays.copyOfRange(num_list, slicer[0], num_list.length);
        } else if (n == 3) {
            return Arrays.copyOfRange(num_list, slicer[0], slicer[1] + 1);
        } else {
            for(int i = slicer[0]; i <= slicer[1]; i += slicer[2]) {
                list.add(num_list[i]);   
            }
            int[] answer = new int[list.size()];
            
            for(int i = 0; i < list.size(); i++){
                answer[i] = list.get(i);
            }
            return answer;
        }
    }
}