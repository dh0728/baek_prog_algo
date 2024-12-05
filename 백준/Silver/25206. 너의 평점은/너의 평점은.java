//BufferedReader 사용하는 방법
//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        //BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        //readLine() 사용해서 한줄 다 받아오기
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        double cnt=0;
        double sum_score=0;
        String[] grade_list = {"F","O","D0","D+","C0","C+","B0","B+","A0","A+"};
        for(int i=0;i<20;i++){
            String[] subject = in.readLine().split(" ");
            double score = Double.parseDouble(subject[1]);

            for(int j=0;j<grade_list.length;j++){
                if (subject[2].equals(grade_list[j])){
                  cnt+=score;
                  double score_grade = (j*0.5)*score;
                  sum_score += score_grade;
                }
            }
        }
        System.out.println(sum_score/cnt);
    }
}