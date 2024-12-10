//BufferedReader 사용하는 방법
import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        //BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        //BufferedReader in = new BufferedReader(new FileReader("input.txt")); // 파일 입력 설정
        //readLine() 사용해서 한줄 다 받아오기
        //StringTokenizer st = new StringTokenizer(in.readLine()); 공백기준으로 문자열 자르기

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        long M = Integer.parseInt(st.nextToken());
        long N = Integer.parseInt(st.nextToken());

        long cnt =0;
        long x=0;
        long y=0;

        //꺾인 횟수부터 찾기
        if (M>N){
            cnt=(N-1)*2+1;
        } else{
            cnt=(M-1)*2;
        }

        // 마지막 지점 찾기
        if (M==N){ // 가로 세로 길이 같을 때
            if(M%2==0){
                x = (long) M/2 + 1;
                y = (long) M/2;
            } else{ // 홀수 일 때
                x = (long) (M-1)/2 + 1;
                y = (long) (M-1)/2 + 1;
            }
        } else{
            if(M>N){
                if(N%2==0){
                    x = (long) N/2+1;
                    y = (long) N/2;
                } else{
                    x = (long) N/2+1 + (M-N);
                    y = (long) N/2+1;
                }
            } else{
                if(M%2==0){
                    x = (long) M/2+1;
                    y = (long) M/2;
                } else{
                    x = (long) M/2+1;
                    y = (long) M/2+1 + (N-M);
                }
            }
        }
        System.out.println(cnt);
        System.out.println(x + " " +y);

    }
}
