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
        String words = in.readLine();

        String[] cro = {"c=","c-","dz=","d-","lj","nj","s=","z="};

        for(int i=0; i<cro.length; i++){
            if (words.contains(cro[i])){
                words = words.replace(cro[i], "!");
            }
        }
        System.out.println(words.length());
    }
}