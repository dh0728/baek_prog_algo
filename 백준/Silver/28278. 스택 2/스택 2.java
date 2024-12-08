//BufferedReader 사용하는 방법
//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// FileReader 사용하기 위해 임포트
import java.io.*;

import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader in = new BufferedReader((new InputStreamReader(System.in)));
        int N = Integer.parseInt(in.readLine());
        Stack<Integer> stack = new Stack<>();
        for(int i=0;i<N;i++){
            StringTokenizer st = new StringTokenizer(in.readLine());
            int com = Integer.parseInt(st.nextToken());
            if (com ==1){
                int num = Integer.parseInt(st.nextToken());
                stack.push(num);
            } else if (com==2){
                if (stack.empty()){
                    System.out.println(-1);
                }else{
                    System.out.println(stack.pop());
                }
            } else if (com==3){
                System.out.println(stack.size());
            } else if(com==4){
                if (stack.empty()){
                    System.out.println(1);
                }
                else {
                    System.out.println(0);
                }
            } else if (com==5) {
                if (stack.empty()){
                    System.out.println(-1);
                } else {
                    System.out.println(stack.peek());
                }
            }
        }

    }

}