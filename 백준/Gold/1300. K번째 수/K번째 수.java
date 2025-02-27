import java.io.*;

public class Main {

    static long N;
    static long K;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        K = Integer.parseInt(br.readLine());

        long result = findNumber();
        System.out.println(result);
    }

    public static long findNumber(){

        long left = 1;
        long right = N * N;
        long res = 0;

        long cnt =0;
        while (left <= right){

//            System.out.println("left: " + left + ", right: " + right);
            long mid = (left + right)/2 ;

            // 배열 row 별로 mid보다 작거나 같은 수의 개수를 세기
            cnt = calculateLower(mid);

            if (cnt >= K){
                right = mid - 1;
                res = mid;
            } else {
                left = mid + 1;
            }
        }
        return res;
    }
    private static long calculateLower(long mid){
        long cnt =0;

        for (int i =1; i<=N; i++){
            long num = mid/i;
            cnt += Math.min(num,N);
        }
//        System.out.println("mid: " + mid + ", cnt: " + cnt);
        return cnt;
    }

}

