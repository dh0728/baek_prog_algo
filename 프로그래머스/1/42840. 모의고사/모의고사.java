import java.util.Arrays;
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] answers) {
        int[] student1 = {1,2,3,4,5};
        int[] student2 = {2,1,2,3,2,4,2,5};
        int[] student3 = {3,3,1,1,2,2,4,4,5,5};

        int[] answer = new int[3];
        answer[0] = count_answer(student1, answers);
        answer[1] = count_answer(student2, answers);
        answer[2] = count_answer(student3, answers);
        
        //최댓값 찾기
        int max_answer = Arrays.stream(answer).max().getAsInt();
        
        ArrayList<Integer> resultList = new ArrayList<>();
        
        for(int i=0; i<answer.length;i++){
            if (answer[i]==max_answer){
                resultList.add(i+1);
            }
        }
        
        int[] result = resultList.stream().mapToInt(i->i).toArray();
        return result;
    }
    int count_answer(int[] student, int[] answers) {
        int cnt =0;
        int len = student.length;
        for(int i=0; i<answers.length; i++){
            if (student[i%len] == answers[i]){
                cnt +=1;
            }
        }
        return cnt;
    }
}