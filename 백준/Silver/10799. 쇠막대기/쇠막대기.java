//BufferedReader 사용하는 방법
//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//import java.util.StringTokenizer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import java.util.Stack;



public class Main {
    public static void main(String[] args) throws IOException {
        //BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        //readLine() 사용해서 한줄 다 받아오기
        //StringTokenizer st = new StringTokenizer(in.readLine()); 공백기준으로 문자열 자르기

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String pipes = in.readLine().replace("()","O");

        Stack<Character> stack = new Stack<>();

        int cnt=0;
        int pipe_cnt=0;
        for(int i=0;i<pipes.length();i++){
            char p= pipes.charAt(i);
            if(p=='('){
                pipe_cnt +=1;
                stack.push(p);
            }else if(p==')'){
                stack.pop();
            }else{
                cnt +=stack.size();
            }
        }
        cnt += pipe_cnt;
        System.out.println(cnt);


    }
}