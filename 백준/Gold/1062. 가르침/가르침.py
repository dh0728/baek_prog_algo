import sys
input=sys.stdin.readline

def check_word():
    cnt=0
    for word in words:
        is_read=True
        for a in word:
            if not alpha[ord(a)-97]: # 가르침을 못닫은 알파벳이 있는 단어면
                is_read=False
                break
        if is_read:
            cnt+=1
    return cnt
def dfs(start,depth):
    global max_cnt

    if depth == K-5: # 가르침 받은 알파벳 수 만큼 탐색했으면
        cnt= check_word()
        if cnt > max_cnt: # 현재 가르침 받은 알파벳으로 읽을 수 있는
            max_cnt=cnt  # 단어가 이전 결과보다 많다면 바꾸기
        return

    for i in range(start,26): # 학습할 단어 순회로 탐색
        if alpha[i]: # 이미 학습한 알파벳으면 패스
            continue
        alpha[i]=1 # 학습 처리
        dfs(i,depth+1) # 다음 학습 단어 재귀 호출
        alpha[i]=0 # 다음 순회를 위해 다시 미학습 처리


N,K=map(int,input().split()) # N : 단어의 개수 K: 가르침 받은 글자 수

if K < 5: # 가르침 받은 알파벳 수가 5보다 작으면 암것도 가르침 못받음
    print(0)
elif K >= 26: # 26개 이상 이면 모든 단어 다 읽을 수 있음
    print(N)
else:
    words=[]
    for _ in range(N):
        word = input().strip()
        word = word[4:-4] # 앞뒤 필요 없는 알파벳 빼주기
        words.append(word)

    # a ~ z = 97 ~ 122
    max_cnt=0
    alpha = [0] * 26
    # 단어 앞뒤 항상 anti, tica이므로 a,n,t,i,c 최소 5글자는 필수로 알고 있어야 함
    for a in 'antic':
        alpha[ord(a)-97]=1

    dfs(0,0) # start, depth
    print(max_cnt)