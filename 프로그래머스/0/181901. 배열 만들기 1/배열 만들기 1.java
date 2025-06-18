import java.util.ArrayList;
import java.util.stream.*;

class Solution {
    public int[] solution(int n, int k) {
        
        ArrayList<Integer> list = new ArrayList<>();
        
        for(int i = k; i <= n; i+=k){
            list.add(i);
        }
        int[] answer = list.stream().mapToInt(Integer::intValue).toArray();
        
        return answer;
    }
}