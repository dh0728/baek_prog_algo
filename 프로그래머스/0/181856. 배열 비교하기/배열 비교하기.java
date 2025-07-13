class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int arr1_len = arr1.length;
        int arr2_len = arr2.length;
        
        if(arr1_len == arr2_len) { //길이같으면
            int arr1_sum = 0;
            int arr2_sum = 0;
            for(int i = 0; i < arr1_len; i++) {
                arr1_sum += arr1[i];
                arr2_sum += arr2[i];
            }
            return arr1_sum == arr2_sum ? 0 : arr1_sum > arr2_sum ? 1 : -1;
        } else { // 길이다르면
            return arr1_len > arr2_len ? 1 : -1;
        }
    }
}