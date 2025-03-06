import java.io.*;

import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    static int N;
    static int M;
    static int[][] maps;
    static int[][] dp;
    static int[][] dxy = {{1,0}, {0,1}, {-1,0}, {0,-1}};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        maps = new int[N][M];
        dp = new int[N][M];


        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0 ; j < M; j++) {
                maps[i][j] = Integer.parseInt(st.nextToken());
                dp[i][j] = -1;
            }
        }
        int result = DFS(0,0);

        System.out.println(result);

    }

    private static int DFS(int x, int y){

        if (x == N-1 && y == M-1) { //목적지 도착하면
            return 1;
        }

        if (dp[x][y] != -1){ //이미 방문한 적이 있는 곳이면
            return dp[x][y];
        } else {
            dp[x][y] = 0;
            for (int k = 0; k < 4; k++) {
                int nx = x + dxy[k][0];
                int ny = y + dxy[k][1];
                if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue; //범위 벗어나는 것은 패스

                if (maps[nx][ny] < maps[x][y]) { //갈수 있는 길이면 재귀
                    dp[x][y] += DFS(nx, ny);
                }
            }

        }
        return dp[x][y];
    }
}

