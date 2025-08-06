class Solution {
    public int solution(String[] strArr) {
        int[] lens_list = new int[31];
        int answer = 0;
        
        for(int i = 0; i < strArr.length; i++){
            lens_list[strArr[i].length()] += 1;
        }
        
        for(int i = 0; i < lens_list.length; i++){
            if ( answer < lens_list[i]) {
                answer = lens_list[i];
            }
        }
        
        
        return answer;
    }
}