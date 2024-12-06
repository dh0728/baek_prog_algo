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
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        int x=1;
        int y=1;
        int max_num =0;
        for(int i=1;i<=9;i++){
            StringTokenizer st = new StringTokenizer(in.readLine());
            for (int j=1; j<=9;j++){
                int n = Integer.parseInt(st.nextToken());
                if (n >max_num){
                    x=i;
                    y=j;
                    max_num=n;
                }

            }
        }
        System.out.println(max_num);
        System.out.println(x +" "+ y);
    }
}