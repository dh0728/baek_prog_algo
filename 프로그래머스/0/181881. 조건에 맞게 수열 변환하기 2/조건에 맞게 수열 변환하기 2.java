class Solution {
    public int solution(int[] arr) {
        
        int answer = 0;
        
        while(true) {
            int[] temp = transArr(arr);
            answer +=1;
            
            if(comparArr(arr, temp)) { // 아직 더 변환해야함
                answer -=1;
                break;
            } else {
                arr = temp;
                continue;
            }
        }
        return answer;
    }
    
    private int[] transArr(int[] arr){
        int[] result = new int[arr.length];
        for(int i = 0; i < arr.length; i++){
            if(arr[i] >= 50 && arr[i] % 2 == 0) {
                result[i] = arr[i]/2; 
            } else if (arr[i] < 50 && arr[i] %2 == 1){
                result[i] = arr[i]*2 + 1;
            } else {
                result[i] = arr[i];
            }
        }
        return result;
    }
    
    private boolean comparArr(int[] arr1, int[] arr2){
        for(int i = 0; i < arr1.length; i++){
            if(arr1[i] != arr2[i]) {
                return false;
            }
        }
        return true;
    }
}