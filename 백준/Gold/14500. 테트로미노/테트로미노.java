import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
//        BufferedReader in = new BufferedReader(new FileReader("input.txt"));
        StringTokenizer st = new StringTokenizer(in.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] maps = new int[N][M];

        for(int i=0;i<N;i++){
            StringTokenizer numbers = new StringTokenizer(in.readLine());
            for(int j=0;j<M;j++){
                int n= Integer.parseInt(numbers.nextToken());
                maps[i][j]=n ;
            }
        }

        int[][][][] shapes ={ // I,O,L,T,Z순으로 들어있음
                {
                        {{0, 0}, {0, 1}, {0, 2}, {0, 3}},
                        {{0, 0}, {1, 0}, {2, 0}, {3, 0}},
                },
                {
                        {{0, 0}, {0, 1}, {1, 0}, {1, 1}},
                },
                {
                        {{0, 0}, {0, -1}, {0, 1}, {-1, 1}},
                        {{0, 0}, {0, -1}, {0, 1}, {1, 1}},

                        {{0, 0}, {0, -1}, {0, 1}, {-1, -1}},
                        {{0, 0}, {0, -1}, {0, 1}, {1, -1}},

                        {{0, 0}, {-1, 0}, {1, 0}, {-1, 1}},
                        {{0, 0}, {-1, 0}, {1, 0}, {1, 1}},

                        {{0, 0}, {-1, 0}, {1, 0}, {-1, -1}},
                        {{0, 0}, {-1, 0}, {1, 0}, {1, -1}},
                },
                {
                        {{0, 0}, {0, -1}, {0, 1}, {-1, 0}},
                        {{0, 0}, {0, -1}, {0, 1}, {1, 0}},
                        {{0, 0}, {-1, 0}, {1, 0}, {0, 1}},
                        {{0, 0}, {-1, 0}, {1, 0}, {0, -1}},

                },
                {
                        {{0, 0},{0, -1},{1, 0},{1, 1}},
                        {{0, 0},{0, -1},{-1, 0},{-1, 1}},

                        {{0, 0},{-1, 0},{0, 1},{1, 1}},
                        {{0, 0},{-1, 0},{0, -1},{1, -1}},

                }
        };
        int max_sum=0;
        for(int i=0;i<N;i++){
            int sum=0;
            for(int j=0;j<M;j++){
                for(int z=0;z<shapes.length;z++){
                    sum=cnt_max(i,j,shapes[z],maps,N,M);
                    if(sum>max_sum){
                        max_sum=sum;
                    }
                }
            }
        }
        System.out.println(max_sum);

    }
    static int cnt_max(int x,int y,int[][][] shapes,int[][] maps,int N, int M){
        int max_sum=0;
        for(int i=0;i<shapes.length;i++){
            int sum=0;
            boolean is_val=true;
            for(int j=0;j<shapes[i].length;j++){
                int nx= x+ shapes[i][j][0];
                int ny= y+ shapes[i][j][1];
                if(nx <0 || nx>=N || ny<0 || ny>=M){
                    is_val =false;
                    break;
                }
                sum +=maps[nx][ny];
            }
            if(is_val && sum >max_sum){
                max_sum=sum;
            }
        }
        return max_sum;
    }
}