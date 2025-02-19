import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int solution(int[] mats, String[][] park) {
        int park_row = park.length;
        int park_col = park[0].length;
        
        int answer = -1;

        for (int mat : mats) { // 돗자리 하나씩 시도
            for (int i = 0; i < park_row; i++) {
                for (int j = 0; j < park_col; j++) {
                    if ("-1".equals(park[i][j])) {
                        if (find_sit(i, j, mat, park, park_row, park_col)) {
                             if(answer < mat) 
                                answer = mat;

                        }
                    }
                }
            }
        }

        return answer; // 모든 돗자리를 깔 수 없는 경우
    }

    public boolean find_sit(int i, int j, int mat, String[][] park, int park_row, int park_col) {
        // `mat x mat` 크기의 돗자리를 깔 수 있는지 확인
        for (int x = 0; x < mat; x++) {
            for (int y = 0; y < mat; y++) {
                int ni = i + x; // 행 이동
                int nj = j + y; // 열 이동
                
                // 공원 범위를 벗어나거나, 해당 위치가 이미 차있다면 돗자리 배치 불가
                if (ni >= park_row || nj >= park_col || !"-1".equals(park[ni][nj])) {
                    return false;
                }
            }
        }
        return true; // 돗자리 배치 가능
    }
}
