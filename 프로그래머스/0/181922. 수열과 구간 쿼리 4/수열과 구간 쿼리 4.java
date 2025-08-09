class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = {};
        
        for(int j=0; j < queries.length; j++) {
            for(int i=0; i < arr.length; i++ ) {
                if (i >= queries[j][0] && i <= queries[j][1]) {
                    if (i% queries[j][2] == 0) {
                        arr[i] += 1;
                    }
                }    
            }
            
        }
        return arr;
    }
}