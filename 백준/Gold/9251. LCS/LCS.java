import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static int[][] dp;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String sub1 = br.readLine();
        String sub2 = br.readLine();

        int sub1Len = sub1.length();
        int sub2Len = sub2.length();

        dp = new int[sub1Len + 1][sub2Len + 1];

        for (int i = 0; i < sub1Len; i++) {
            for (int j = 0; j < sub2Len; j++) {
                if (sub1.charAt(i) == sub2.charAt(j)) {
                    dp[i + 1][j + 1] = dp[i][j] + 1;
                } else {
                    dp[i + 1][j + 1] = Math.max(dp[i][j + 1], dp[i + 1][j]);
                }
            }
        }
        System.out.println(dp[sub1Len][sub2Len]);


    }
}