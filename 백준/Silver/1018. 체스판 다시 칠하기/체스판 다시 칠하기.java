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

        int WB_cnt=change_cnt(WB,maps,N,M);
        int BW_cnt=change_cnt(BW,maps,N,M);

        if (WB_cnt > BW_cnt){
            System.out.println(BW_cnt);
        }else{
            System.out.println(WB_cnt);
        }
    }
    static int change_cnt(char[][] color, char[][] maps , int N, int M ){
        int min_cnt =1000000;
        for(int x=0; x<N-7; x++){
            for(int y=0; y<M-7; y++){
                // 갯수 비교시작
                int cnt =0;
                for(int i=x; i<x+8; i++){
                    if(cnt>min_cnt){ // cnt가 크면 더이상 계산 x
                        break;
                    }
                    for(int j=y; j<y+8; j++){
                        if(color[(i-x)%2][j-y] != maps[i][j]){
                            cnt +=1;
                        }
                    }
                }
                min_cnt=Math.min(min_cnt, cnt);;
            }
        }
        return min_cnt;
    }
}