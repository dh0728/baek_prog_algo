//BufferedReader 사용하는 방법
//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        //BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        //readLine() 사용해서 한줄 다 받아오기
        //StringTokenizer st = new StringTokenizer(in.readLine()); 공백기준으로 문자열 자르기

        BufferedReader in = new BufferedReader((new InputStreamReader(System.in)));
        StringTokenizer st = new StringTokenizer(in.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        char[][] maps = new char[N][M];

        for(int i=0;i<N;i++){
            String line = in.readLine();
            for(int j=0;j<M;j++){
                maps[i][j]= line.charAt(j);
            }
        }
        char[][] WB = {
                {'W','B','W','B','W','B','W','B'},
                {'B','W','B','W','B','W','B','W'}
        };

        char[][] BW = {
                {'B','W','B','W','B','W','B','W'},
                {'W','B','W','B','W','B','W','B'}
        };

        int min_cnt=1000000;
        for(int x=0; x<N-7; x++){
            for(int y=0; y<M-7; y++) {
                int WB_cnt=change_cnt(maps,WB,x,y,min_cnt);
                int BW_cnt=change_cnt(maps,BW,x,y,min_cnt);
                min_cnt=Math.min(min_cnt, WB_cnt);;
                min_cnt=Math.min(min_cnt, BW_cnt);;
            }
        }
        System.out.println(min_cnt);
    }
    static int change_cnt(char[][] maps,char[][] color, int x, int y,int min_cnt ) {
        int cnt = 0;
        for (int i = x; i < x + 8; i++) {
            for (int j = y; j < y + 8; j++) {
                if (cnt > min_cnt){
                    return min_cnt;
                }
                if (color[(i - x) % 2][j - y] != maps[i][j]) {
                    cnt += 1;
                }
            }
        }
        return cnt;
    }
}