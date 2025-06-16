class Solution {
    public int[] solution(int[] num_list, int n) {
        int[] arr1 = new int[num_list.length - n];
        int[] arr2 = new int[n];
        for(int i =0; i < num_list.length; i++) {
            if (i < n) {
                arr2[i] = num_list[i];
            } else {
                arr1[i - n] = num_list[i];
            }
        }
        
        int[] answer = new int[arr1.length + arr2.length];
        
        System.arraycopy(arr1, 0, answer, 0, arr1.length);
        System.arraycopy(arr2, 0, answer, arr1.length, arr2.length);
        
        return answer;
    }
}