import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    static int N;
    static int[] arr;
    static List<Integer> LFS = new ArrayList<>();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        arr = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken());
            arr[i] = num;
        }

        // 초기값은 첫 번째값을 넣어야함
        LFS.add(arr[0]);
        int len = LFS.size();

        for (int i = 1; i < N; i++) {
            int num = arr[i];
            if (num > LFS.get(len-1)){
                LFS.add(num);
                len++;
            } else {
                findNum(num, len);
            }
        }
        System.out.println(LFS.size());
    }
    private static void findNum(int num, int len){
        int left = 0;
        int right = len - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (LFS.get(mid) < num){
                left = mid + 1;
            } else if (LFS.get(mid) > num){
                right = mid - 1;
            } else {
                return;
            }
        }
        LFS.set(left, num);
        return;
    }



}

