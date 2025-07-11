class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        String newPat = "";
        for(int i = 0; i < pat.length(); i++) {
            if( pat.charAt(i) == 'A') {
                newPat += "B";
            } else {
                newPat += "A";
            }
        }
        if( myString.contains(newPat)) {
            answer = 1; 
        }        
        return answer;
    }
}