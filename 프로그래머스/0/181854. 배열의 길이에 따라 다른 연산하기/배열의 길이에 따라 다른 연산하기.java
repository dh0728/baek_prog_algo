class Solution {
    public int[] solution(int[] arr, int n) {
        int x = 1;
        if (arr.length % 2 == 1) { // 홀수
            x = 0;
        }
        for(int i = x; i < arr.length; i +=2) {
            arr[i] += n;
        }
        return arr;
    }
}