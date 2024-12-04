//Scanner 사용하는 방법
//import java.util.Scanner;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        //Scanner in = new Scanner(System.in);

        // nextInt() 정수한개
        // next() 단어
        // nextLine() 한줄
        Scanner in = new Scanner(System.in);
        String word = in.next();
        int word_len = word.length();
        int cnt = (int) word_len/2; //홀수도 고려
        int result =1;
        for (int i=0;i<cnt;i++){
            int end = word_len-1-i;
            char front_alp = word.charAt(i);
            char end_alp = word.charAt(end);
            if (front_alp != end_alp){
                result =0;
                break;
            }
        }
        System.out.println(result);
    }
}