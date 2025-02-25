import java.io.*;
import java.util.Arrays;
import java.util.Collections;


public class Main {

    static int N;
    static int[] arr;
    static int account;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N];

        String[] str = br.readLine().split(" ");

        for (int i =0 ; i < N ; i++){
            int num = Integer.parseInt(str[i]);
            arr[i] = num;
        }

        Arrays.sort(arr); //정렬하기

        account = Integer.parseInt(br.readLine());


        // 이진 탐색을 이용한 상한액 결정
        int result = findUpperLimit();
        System.out.println(result);


    }
    public static int findUpperLimit(){
        int left = 0;
        int right = arr[N-1];
        int ans = 0;

        while (left <= right) {
            int mid = ( left +right ) / 2;
            int sum = 0;

            for (int i = 0 ; i < N ; i++){
                sum += Math.min(arr[i], mid);
            }

            if (sum <= account){ //상한선 올리기
                ans = mid;
                left = mid + 1;
            } else { // 상한선 내리기
                right = mid - 1;
            }
        }
        return ans;
    }

}

