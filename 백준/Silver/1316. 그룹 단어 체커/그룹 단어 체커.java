//BufferedReader 사용하는 방법
//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException{
        //BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        //readLine() 사용해서 한줄 다 받아오기
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        String input = in.readLine();

        int N = Integer.parseInt(input);
        int result =0;
        for(int i=0; i<N;i++){
            String word = in.readLine();
            result += is_group(word);
        }
        System.out.println(result);
    }
    static int is_group(String word){
        int[] alpha = new int[26];
        for(int i=0;i<word.length();i++){
            int n = (int) word.charAt(i);
            if (alpha[n-97] !=0){
                int defore_n = (int) word.charAt(i-1);
                if (defore_n==n){
                    continue;
                }else{
                    return 0;
                }
            }
            alpha[n-97] =1;
        }
        return 1;
    }
}