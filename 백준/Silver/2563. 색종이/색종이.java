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

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(in.readLine());

        int[][] paper =new int[101][101];

        for (int i=0;i<N;i++){
            StringTokenizer st = new StringTokenizer(in.readLine());
            int left = Integer.parseInt(st.nextToken());
            int right = Integer.parseInt(st.nextToken());
            for(int x=left; x<left+10;x++) {
                for (int y = right; y < right + 10; y++) {
                    paper[x][y] += 1;
                }
            }
        }
        int result=0;
        for(int i=1;i<=100;i++){
            for(int j=1;j<=100;j++) {
                if (paper[i][j]>0){
                    result+=1;
                }
            }
        }
        System.out.println(result);
    }
}