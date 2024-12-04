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
        int N = in.nextInt();
        int len = 2*N-1; //별출력횟수
        for (int i=1; i<2*N; i+=2){
            int none_cnt = (len-i)/2;
            for (int j=0; j<none_cnt;j++) {
                System.out.print(" ");
            }
            System.out.print("*".repeat(i));
            System.out.println(); //줄바끔
        }
        for(int i=len-2;i>0; i-=2){
            int none_cnt = (len-i)/2;
            for (int j=0; j<none_cnt;j++) {
                System.out.print(" ");
            }
            System.out.print("*".repeat(i));
            System.out.println(); //줄바끔
        }


    }
}