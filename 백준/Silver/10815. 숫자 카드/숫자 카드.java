import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N,M;
    static int[] arr1;

    public static void main(String[] args) throws IOException {

        // 숫자카드 N개
        // 정수 M개
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        //BufferedReader in = new BufferedReader(new FileReader("input.txt"));
        StringTokenizer st = new StringTokenizer(in.readLine());
        N = Integer.parseInt(st.nextToken()); // 5

        String[] str_arr1= in.readLine().split(" "); // 6 3 2 10 -10
        arr1 = new int[N];

        for (int i = 0; i < N; i++) {
            arr1[i] = Integer.parseInt(str_arr1[i]);
        }

        Arrays.sort(arr1);

        st = new StringTokenizer(in.readLine());
        M = Integer.parseInt(st.nextToken()); // 8
        String[] str_arr2= in.readLine().split(" "); // 10 9 -5 2 3 4 5 -10

        int[] result = new int[M];

        for (int i = 0; i< M; i++) {
            int num = Integer.parseInt(str_arr2[i]);
            result[i] = BinarySearch(num);
            System.out.print(result[i] + " ");
        }



    }
    public static int BinarySearch(int num){
        int left =0;
        int right = N-1;

        while (left <= right){
            int mid = (left + right)/2;
            int middleValue = arr1[mid];

            if (num > middleValue){
                left = mid + 1;
            } else if (num < middleValue) {
                right = mid - 1;
            } else return 1;
        }
        return 0;
    }

}

