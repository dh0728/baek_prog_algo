class Solution {
    
    static int[] is_success;
    
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;
        int N = schedules.length;
        
        is_success = new int[N];
            
        // 모두 받을 수 있다는 상태로 시작
        for(int i = 0; i < N ; i++){
            is_success[i] = 1;
        }
        
        for(int i = 0; i < N; i++) {
            int today = startday;
            for(int j = 0; j < 7; j++){
                if (is_success[i] == 0) break; // 이미 못받는 친구면 패스
                
                if (today < 6) {
                    if ( !calculateLimit(schedules[i], timelogs[i][j]) ){
                        is_success[i] = 0;
                    }
                } 
                today = (today % 7) + 1;

            }
        }
        
        for (int i = 0; i < N; i++){
            if (is_success[i] == 1){
                answer++;
            }
        }
        
        return answer;
    }
    
    public static boolean calculateLimit(int time, int timelog){
        int min_time = time % 100;
        int hour_time = time / 100;
        
        int sec_time = min_time * 60 + hour_time * 3600;
        
        int min_timelog = timelog % 100;
        int hour_timelog = timelog / 100;
        
        int sec_timelog = min_timelog * 60 + hour_timelog * 3600;
        
        int diff = sec_timelog - sec_time;
        
        if ( diff > 600){
            return false;
        }
        
        return true;
        
    }
    
}