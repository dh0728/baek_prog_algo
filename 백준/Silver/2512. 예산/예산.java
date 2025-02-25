import java.io.*;
import java.util.Arrays;
import java.util.Collections;


public class Main {

    static int N;
    static int total =0;
    static Integer[] arr;
    static int account;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new Integer[N];

        String[] str = br.readLine().split(" ");

        for (int i =0 ; i < N ; i++){
            int num = Integer.parseInt(str[i]);
            arr[i] = num;
            total += num;
        }

        Arrays.sort(arr , Collections.reverseOrder()); //정렬하기

        account = Integer.parseInt(br.readLine());

        if (account >= total){ //모든 요청이 배정될 수 있는 경우
            System.out.println(arr[0]);
        }else{
            int top = arr[0]-1;
            while (true){
                total =0;
                for (int i=0 ; i < N ; i++){
                    if (arr[i] >= top){ //상한선 보다 크면
                        total += top;
                    } else{
                        total += arr[i];
                    }

                }
                if (total > account){ //예산을 초과하면 다시 시작
                    top -=1;
                }
                else {
                    break;
                }
            }
            System.out.println(top);
        }

    }

}

