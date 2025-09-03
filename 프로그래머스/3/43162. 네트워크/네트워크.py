from collections import deque

def dfs(n, nodes):
    
    cnt = 0;
    visited = [0] * (n + 1) # 방문 체크
    
    stack = []
    for i in range(n):
        if visited[i] : # 방문했으면
            continue
            
        current_node = i
        cnt += 1
        visited[i] = 1 # 방문표시하기
        stack.append(i)
        while stack:
            current_node = stack.pop()
            
            for j in range(n):
                if nodes[current_node][j] == 0 or i == j: # 연결 안된건 패스
                    continue
                    
                if visited[j] == 1:  # 방문한적이 있으면
                    continue
                stack.append(j)
                # current_node = j
                visited[j] = 1
    
    return cnt
                    
    

def solution(n, computers):

    answer = dfs(n, computers)
    
    return answer