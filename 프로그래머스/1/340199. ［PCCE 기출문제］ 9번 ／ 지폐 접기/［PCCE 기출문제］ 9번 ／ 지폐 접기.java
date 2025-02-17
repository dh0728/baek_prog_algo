class Solution {
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;
        int wallet_min = wallet[0] < wallet[1] ? wallet[0] : wallet[1];
        int wallet_max = wallet[0] < wallet[1] ? wallet[1] : wallet[0];
        
        int bill_min = bill[0] < bill[1] ? bill[0] : bill[1];
        int bill_max = bill[0] < bill[1] ? bill[1] : bill[0];
        while (true){
            if (bill_min > bill_max){
                int temp= bill_min;
                bill_min = bill_max;
                bill_max = temp;
            }
            
            if (bill_min > wallet_min || bill_max > wallet_max) {
                double half_num = bill_max/2;
                bill_max =  (int) Math.floor(half_num);
                answer+=1;
            } else{
                break;

            }   
        }
        return answer;
    }
}