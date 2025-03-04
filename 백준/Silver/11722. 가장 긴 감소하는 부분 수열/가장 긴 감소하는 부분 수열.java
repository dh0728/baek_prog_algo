import java.io.*;

import java.util.StringTokenizer;

public class Main {

    static int N;
    static int[] arr;
    static int[] dp;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        arr = new int[N];
        dp = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i =0; i < N; i++){
            int n = Integer.parseInt(st.nextToken());
            arr[i]= n;
            dp[i]= 1;
        }

        for (int i = 1; i < N; i++ ){
            for (int j =0; j < i; j++){
                if (arr[i] < arr[j] && dp[i] <= dp[j]){ // 전에 더 큰수가 있으면 +1
                    dp[i] = dp[j] + 1;
                } else if (arr[i] == arr[j]) { // 전에 같은 수가 나온적있으면 그거 복사
                    dp[i] = dp[j];
                }
                // 더 큰 경우는 그냥 1인데 이미 1로 초기화 되어있으므로 생략
            }
        }

        int result = 0;
        for (int i = 0; i < N; i++) {
            result = Math.max(dp[i],result);
        }

        System.out.println(result);

    }


}

