import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static long[] arr;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        if (N == 0)
            System.out.println(0);
        else if (N == 1) {
            System.out.println(1);
        } else{

            arr = new long[N+1];

            arr[0] = 0;
            arr[1] = 1;

            for (int i = 2; i < N+1; i++) {
                arr[i] = arr[i - 1] + arr[i - 2];
            }

            System.out.println(arr[N]);
        }





    }
}