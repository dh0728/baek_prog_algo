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
        int N = in.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = in.nextInt();
        }
        //선택정렬
        for (int i = 0; i < N - 1; i++) {
            for (int j = i+1; j < N; j++) {
                if (arr[i] > arr[j]) {
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        for (int i : arr) {
            System.out.println(i);
        }
    }
}