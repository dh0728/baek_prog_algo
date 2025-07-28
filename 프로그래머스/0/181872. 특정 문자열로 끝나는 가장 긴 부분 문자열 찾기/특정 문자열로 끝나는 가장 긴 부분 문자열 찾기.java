class Solution {
    public String solution(String myString, String pat) {
        int lastIndex = -1;

        // 뒤에서부터 패턴을 찾음
        for (int i = myString.length() - pat.length(); i >= 0; i--) {
            if (myString.substring(i, i + pat.length()).equals(pat)) {
                lastIndex = i + pat.length() - 1;  // 패턴 끝 인덱스
                break;
            }
        }

        // 부분 문자열 반환
        return myString.substring(0, lastIndex + 1);
    }
}
