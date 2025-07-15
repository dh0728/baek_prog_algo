class Solution {
    public int solution(String binomial) {
        String[] arr = binomial.split(" ");
        int num1 = Integer.parseInt(arr[0]);
        int num2 = Integer.parseInt(arr[2]);
    
        return arr[1].equals("+") ? (num1 + num2) : arr[1].equals("-") ? (num1 - num2) : (num1 * num2);
    }
}