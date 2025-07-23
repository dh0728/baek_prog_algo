import java.util.ArrayList;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        ArrayList<Integer> list = new ArrayList<>();
        
        String num = "";
        for(int i = 0; i < intStrs.length; i++) {
            for(int j = s; j < s + l; j++){
                num += intStrs[i].charAt(j);
            }
            int n = Integer.parseInt(num);
            if (n > k) {
                list.add(n);
            }
            num = "";
        }
        int[] answer = new int[list.size()];
        
        for(int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}