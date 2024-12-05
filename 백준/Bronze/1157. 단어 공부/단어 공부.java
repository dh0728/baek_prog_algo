//Scanner 사용하는 방법
//import java.util.Scanner;

import java.util.Arrays;
import java.util.Scanner;

//1157 단어공부
public class Main {
    public static void main(String[] args) {
        //Scanner in = new Scanner(System.in);

        // nextInt() 정수한개
        // next() 단어
        // nextLine() 한줄
        Scanner in = new Scanner(System.in);
        char[] alphabets = in.nextLine().toCharArray();
        //System.out.println(Arrays.toString(alphabets));
        int[] cnt_list = new int[26];
        for (char alphabet : alphabets) {
            int num = (int) alphabet;
            if (num <91){ // 대문자이면
                cnt_list[num-65]+=1;
            } else{
                cnt_list[num-97]+=1;
            }
        }

        int cnt =0;
        int same =0;
        int max=0;
        for (int i=0; i<26 ; i++) {
            if (cnt_list[i] > cnt) {
                cnt =cnt_list[i];
                same =0;
                max=i;
            }else if (cnt==cnt_list[i]) {
                same +=1;
            }
        }
        if (same == 0){
            System.out.println((char) (max+65));
        } else {
            System.out.println("?");
        }

    }
}