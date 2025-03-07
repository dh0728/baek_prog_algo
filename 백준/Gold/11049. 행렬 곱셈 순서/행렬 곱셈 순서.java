import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int N;
    static int[][] matrices;
    static long[][] dp;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        matrices = new int[N + 1][2];
        dp = new long[N + 1][N + 1];

        for (int i = 1; i <= N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            matrices[i][0] = Integer.parseInt(st.nextToken());
            matrices[i][1] = Integer.parseInt(st.nextToken());

        }

        // 바로 옆 행렬끼리 곱하는 경우
        for (int i = 1; i < N; i++) {
            dp[i][i+1] = matrices[i][0] * matrices[i][1] * matrices[i+1][1];
        }


        for (int k = 2; k < N; k++) {
            for (int i = 1; i <= N - k; i++){
                int j = i + k;
                dp[i][j] = Long.MAX_VALUE;

                for (int p = i; p < j; p++){
//                    dp[i][j] = Math.min(dp[i][p] + matrices[i][0] * matrices[p][1] * matrices[j][1], dp[p][j] + matrices[i][0] * matrices[p][0] * matrices[j][1]);
                    dp[i][j] = Math.min(dp[i][j], dp[i][p] + dp[p+1][j] + matrices[i][0] * matrices[p][1] * matrices[j][1]);
                }
            }

        }

        System.out.println(dp[1][N]);

    }
}