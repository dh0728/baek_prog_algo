

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static HashMap<Integer,Integer> maps;
    public static void main(String[] args) throws IOException {

//        BufferedReader in = new BufferedReader(new FileReader("input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        int T =Integer.parseInt(in.readLine());
        for(int i=0;i<T;i++){
            int N= Integer.parseInt(in.readLine());

            maps = new HashMap<Integer,Integer>(); //해시맵 초기화

            Queue<Integer> maxQue = new PriorityQueue<Integer>(Collections.reverseOrder()); //기본이 오름차순이라 리버스해줘야함
            Queue<Integer> minQue = new PriorityQueue<Integer>();

            for (int j = 0; j < N; j++) {
                StringTokenizer st = new StringTokenizer(in.readLine());

                char commend= st.nextToken().charAt(0);
                int num = Integer.parseInt(st.nextToken());
                
                if (commend=='I'){
                    maxQue.offer(num);
                    minQue.offer(num);
                    maps.put(num,maps.getOrDefault(num,0)+1); // 키있으면 그 value 반환, 없으면 0반환
                } else if (commend =='D') {
                    if (maps.size()==0){ // 비어있는지 확인
                        continue;
                    }
                    if (num == 1){ // 최댓값 지우기
                        delete(maxQue);

                    } else if (num == -1) { //최솟값 지우기
                        delete(minQue);
                    }
                }
            }

            // 큐 정리: 유효하지 않은 값 제거
            while (!maxQue.isEmpty() && maps.getOrDefault(maxQue.peek(), 0) == 0) {
                maxQue.poll();
            }
            while (!minQue.isEmpty() && maps.getOrDefault(minQue.peek(), 0) == 0) {
                minQue.poll();
            }

            if (maps.size()==0){
                System.out.println("EMPTY");
            }else{
                int max = maxQue.peek(); // 비어있으면 0
                int min = minQue.peek();
                System.out.println(max + " " +min);
            }

        }
    }
    static void delete(Queue<Integer> que){
        while (!que.isEmpty()){ //올바른 값 찾을 때까지 순회
            int num = que.poll();
            int cnt = maps.getOrDefault(num,0);

            if (cnt==0){
                continue;
            } else{
                if (cnt==1){
                    maps.remove(num); // 중복이 없는 수이면 그냥 제거
                }else{
                    maps.put(num,cnt-1); // 중복이 있는 수이면 cnt -1 빼서 넣기
                }
                break;
            }

        }

    }
}

