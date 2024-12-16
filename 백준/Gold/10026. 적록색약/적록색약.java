import java.io.*;
import java.util.Deque;
import java.util.LinkedList;

public class Main {

    static char[][] maps;
    static int[][] dxy = {{0,1},{1,0},{0,-1},{-1,0}};
    static int[][] visited;
    static int[][] color_visited;
    static int N;
    static int cnt=0;
    static int blind_cnt=0;
    public static void main(String[] args) throws IOException {
//        BufferedReader in = new BufferedReader(new FileReader("input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(in.readLine());

        maps = new char[N][N];
        visited = new int[N][N];
        color_visited = new int[N][N];
        for(int i=0;i<N;i++){
            String st = in.readLine();
            for(int j=0;j<N;j++){
                char c = st.charAt(j);
                maps[i][j]=c;
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (visited[i][j]==0){
                    color_bfs(i,j);
                }
                if (color_visited[i][j]==0){
                    blind_bfs(i,j);
                }
            }
        }
        System.out.println(cnt + " " + blind_cnt);
    }

    static void color_bfs(int i,int j){
        char color = maps[i][j];
        Deque<int[]> deque = new LinkedList<>();
        visited[i][j]=1;
        int[] start= {i,j};
        deque.add(start);

        while (!deque.isEmpty()){
            int[] loc =deque.poll();
            for(int k=0;k<4;k++){
                int nx=loc[0]+dxy[k][0];
                int ny=loc[1]+dxy[k][1];
                if (nx<0 || nx>=N || ny<0 || ny>=N){ //범위 벗어나면 패스
                    continue;
                };
                if (visited[nx][ny] ==1){ //이미 방문했으면 패스
                    continue;
                }
                if (maps[nx][ny]==color){
                    visited[nx][ny]=1;
                    deque.add(new int[] {nx,ny});
                }
            }
        }
        cnt++;
        return;
    }
    static void blind_bfs(int i,int j){
        char color = maps[i][j];
        Deque<int[]> deque = new LinkedList<>();
        color_visited[i][j]=1;
        int[] start= {i,j};
        deque.add(start);

        while (!deque.isEmpty()){
            int[] loc =deque.poll();
            for(int k=0;k<4;k++){
                int nx=loc[0]+dxy[k][0];
                int ny=loc[1]+dxy[k][1];
                if (nx<0 || nx>=N || ny<0 || ny>=N){ //범위 벗어나면 패스
                    continue;
                };
                if (color_visited[nx][ny] ==1){ //이미 방문했으면 패스
                    continue;
                }
                if(color=='B'){
                    if (maps[nx][ny]==color){
                        color_visited[nx][ny]=1;
                        deque.add(new int[] {nx,ny});
                    }
                }else{
                    if (maps[nx][ny] !='B'){
                        color_visited[nx][ny]=1;
                        deque.add(new int[] {nx,ny});
                    }    
                }

            }
        }
        blind_cnt++;
        return;
    }


}