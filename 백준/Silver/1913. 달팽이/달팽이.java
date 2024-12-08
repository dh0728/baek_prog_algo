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
        //BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        //BufferedReader in = new BufferedReader(new FileReader("input.txt")); // 파일 입력 설정
        //readLine() 사용해서 한줄 다 받아오기
        //StringTokenizer st = new StringTokenizer(in.readLine()); 공백기준으로 문자열 자르기

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(in.readLine());
        int num = Integer.parseInt((in.readLine()));

        int[][] snail = new int[N][N];
        int [][] dxy = {{0,-1},{-1,0},{0,1},{1,0}};
        int center = (int) N/2;

        snail[center][center]=1;
        int dir=0;
        int x=center;
        int y=center;

        // 달팽이 채우기
        for(int i=2; i<=N*N;i++){
           int curr_nx= x + dxy[dir%4][0];
           int curr_ny= y + dxy[dir%4][1];
           int next_nx= x + dxy[(dir+1)%4][0];
           int next_ny= y + dxy[(dir+1)%4][1];
           if (snail[next_nx][next_ny] != 0){ // dir이 바꿀수 없는 상황이면
                snail[curr_nx][curr_ny] =i;   // 현재 방향으로 이동
                x = curr_nx;
                y=  curr_ny;
           } else{ // dir을 바꿀 수 있는 상황이면 바꾸기
               snail[next_nx][next_ny] = i;
               x = next_nx;
               y = next_ny;
               dir +=1;
           }
        }

        // 숫자 찾기
        int row=0;
        int col=0;

        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                System.out.print(snail[i][j] + " ");
                if (snail[i][j]==num){
                    row=i+1;
                    col=j+1;
                }
            }
            System.out.println();
        }
        System.out.println(row + " " + col);
    }
}