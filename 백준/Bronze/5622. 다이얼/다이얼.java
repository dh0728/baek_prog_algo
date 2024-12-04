import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        // nextInt() 정수한개
        // next() 단어
        // nextLine() 한줄

        String str = in.nextLine();
        int count = 0;
        int len = str.length();

        for(int i=0; i<len; i++) {
            String s = String.valueOf(str.charAt(i));
            if (s.equals("A") || s.equals("B") || s.equals("C")) {
                count += 3;
            } else if (s.equals( "D") || s.equals("E" )|| s.equals("F")) {
                count += 4;
            } else if (s.equals( "G") || s.equals("H" )|| s.equals("I")) {
                count += 5;
            } else if (s.equals( "J") || s.equals("K" )|| s.equals("L")) {
                count += 6;
            } else if (s.equals( "M") || s.equals("N" )|| s.equals("O")) {
                count += 7;
            } else if (s.equals( "P") || s.equals("Q" )|| s.equals("R") || s.equals("S")) {
                count += 8;
            } else if (s.equals( "T") || s.equals("U" )|| s.equals("V")) {
                count += 9;}
            else if (s.equals( "W") || s.equals("X" )|| s.equals("Y") || s.equals("Z")) {
                count += 10;
            } else {
                count +=8;
            }
        }
        System.out.println(count);
    }
}