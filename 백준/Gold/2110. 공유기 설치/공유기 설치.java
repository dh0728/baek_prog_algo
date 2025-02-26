import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {

    static int N; //집 갯수
    static int C; //공유기 갯수
    static int[] arr;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(arr);

        System.out.println(findUpperDistance());

    }

    public static int findUpperDistance(){

        int left = 1;
        int right = arr[N-1] - arr[0];

        int ans = 0;

        while( left <= right ) {
            int mid = ( right + left ) /2;

            int installNum = calculateInstall(mid);

            if (installNum >= C) { // 설치 개수 많거나 같은면
                left = mid + 1;    // 거리 늘리기
                ans = mid;
            } else {               //설치개수 부족 거리 줄이기
                right = mid - 1;
            }
        }
        return ans;
    }

    public static int calculateInstall(int dis) {

        int cnt = 1;
        int lastLoc = arr[0];

        for (int i = 1; i < N ; i++) {
            if (arr[i] - lastLoc >= dis) {
                cnt++;
                lastLoc = arr[i];
            }
        }
        return cnt;
    }

}

