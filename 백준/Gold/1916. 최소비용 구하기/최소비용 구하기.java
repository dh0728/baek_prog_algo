import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main {

    static int N; // 도시 개수
    static int M; // 버스 개수
    static List<int[]>[] graph; // 그래프 인접 리스트 (목적지, 비용)

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
//        BufferedReader in = new BufferedReader(new FileReader("input.txt"));
        N = Integer.parseInt(in.readLine());
        M = Integer.parseInt(in.readLine());

        // 그래프 초기화
        graph = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        // 그래프 입력
        for (int i = 0; i < M; i++) {
            String[] line = in.readLine().split(" ");
            int start = Integer.parseInt(line[0]);
            int end = Integer.parseInt(line[1]);
            int cost = Integer.parseInt(line[2]);
            graph[start].add(new int[]{end, cost});
        }

        // 출발점과 도착점 입력
        String[] target = in.readLine().split(" ");
        int start = Integer.parseInt(target[0]);
        int end = Integer.parseInt(target[1]);

        // 최소 비용 계산
        int result = dijkstra(start, end);
        System.out.println(result);
    }

    static int dijkstra(int start, int end) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[1])); // (도시, 비용) , 비용을 기준으로 pq 커스텀
        int[] dist = new int[N + 1]; // 최소 비용 저장 배열
        Arrays.fill(dist, 1000000000); // 최댓값으로 다채우기
        dist[start] = 0;

        pq.add(new int[]{start, 0});

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int city = curr[0];
            int cost = curr[1];

            // 현재 경로가 이미 최적 경로보다 크다면 무시
            if (cost > dist[city]) continue;

            for (int[] edge : graph[city]) {
                int next = edge[0];
                int next_cost = cost + edge[1];

                // 더 적은 비용으로 도달 가능하다면 갱신
                if (next_cost < dist[next]) {
                    dist[next] = next_cost;
                    pq.add(new int[]{next, next_cost});
                }
            }
        }

        return dist[end];
    }
}