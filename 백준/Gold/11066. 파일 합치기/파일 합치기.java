import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        while (T-- > 0) {

            int N = Integer.parseInt(br.readLine());

            StringTokenizer st = new StringTokenizer(br.readLine());

            int[] files = new int[N + 1];
            int[] sums = new int[N + 1];
            int[][] dp = new int[N + 1][N + 1];

            for (int i = 1; i < N + 1; i++) {
                files[i] = Integer.parseInt(st.nextToken());
                sums[i] = sums[i - 1] + files[i];
            }

            // dp가 채워지는 경우의 수

            // 1. dp[i][j]에서 i == j 는 0

            // 2. dp[i][j]에서 i+1 = j 인 경우
            for (int i = 1; i < N; i++) {
                dp[i][i+1] = files[i] + files[i + 1];
            }

            // 3. 1, 2번을 제외한 나머지 경우 i-j >=2인 경우
            for (int k = 2; k < N; k++) {
                for (int i = 1; i <= N - k; i++) {
                    int j = i + k;
                    dp[i][j] = Integer.MAX_VALUE; //최대 크기보다 1큰값으로 초기화

                    for (int p = i; p < j; p++ ){
                        dp[i][j] =  Math.min(dp[i][j], dp[i][p] + dp[p + 1][j] + sums[j] - sums[i - 1]);
                    }
                }

            }
            sb.append(dp[1][N]).append("\n");
        }
        System.out.print(sb);

    }
}