import java.io.*;

import java.util.StringTokenizer;

public class Main {

    static int N;
    static int[][] arr;
    static int[] dp;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        arr = new int[N+1][2];

        dp = new int[N+1];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        for (int i = N-1; i >= 0; i--) {
            if (i + arr[i][0] > N) {
                dp[i] = dp[i+1];
            } else {
                dp[i] = Math.max(dp[i+1], arr[i][1] + dp[i + arr[i][0]]);
            }
        }

        System.out.println(dp[0]);




    }


}

