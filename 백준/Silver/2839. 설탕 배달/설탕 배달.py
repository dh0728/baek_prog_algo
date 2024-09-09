N=int(input()) # 배달해야하는 소금 무게 kg

# 3키로와 5킬로 봉지를 이용해 최소한의 봉지로 배달해야한다.
# 정확하게 N 킬로그램을 만들 수 없다면 -1 출력

# 역시나 시간초과
def dfs(cnt,n):
    global result
    if result != -1:
        return
    if n<0: #
        return
    # if cnt >=result: # 봉지수가 현재까지 계산된 최소 봉지보다 커지면 바로 종료
    #     return
    if n==0: # 봉지를 다선택하면
        result=cnt
        return
    for kg in kg_list:
        dfs(cnt+1,n-kg)
    return
kg_list=[5,3]
result=-1
dfs(0,N)
print(result)