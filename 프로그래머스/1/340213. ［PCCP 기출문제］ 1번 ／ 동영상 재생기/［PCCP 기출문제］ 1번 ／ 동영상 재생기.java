class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        String answer = "";
        int videoTime = transTime(video_len);
        int posTime = transTime(pos);
        int opStartTime = transTime(op_start);
        int opEndTime = transTime(op_end);
        
        for(int i=0; i< commands.length; i++){
            if (posTime >= opStartTime && posTime <= opEndTime){ // 오프닝 구간 사이 일 경우
                posTime = opEndTime;
            }
            if (commands[i].equals("prev")){ // 뒤로 가기
                posTime -=10;       
                if (posTime < 0){ // 현재 위치가 10초 미만인 경우
                    posTime =0;
                }
            } else { // 앞으로 가기
                posTime +=10;
                if (posTime >videoTime){ //남은 시간이 10초 미만일 경우
                    posTime = videoTime;
                }
            }
            if (posTime >= opStartTime && posTime <= opEndTime){ // 오프닝 구간 사이 일 경우
                posTime = opEndTime;
            }
        }
        
        return transTimeToString(posTime);
    }
    public int transTime(String time){
        String[] time_split = time.split(":"); // :으로 자르기
        int min = Integer.parseInt(time_split[0]);
        int sec = Integer.parseInt(time_split[1]);
        
        int total_time = min*60 + sec;
        return total_time;
    }
    public String transTimeToString(int time){
        int minInt = time/60;
        int secInt = time%60;
        
        String minStr = Integer.toString(minInt);
        String secStr = Integer.toString(secInt);
        if (minStr.length() ==1){
            minStr = '0'+ minStr;
        }
        if (secStr.length() ==1){
            secStr = '0'+ secStr;
        }
        return minStr + ":" + secStr;
    }
}