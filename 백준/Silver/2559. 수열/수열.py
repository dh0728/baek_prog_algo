N, K=map(int,input().split()) 
# N 온도를 측정한 전체 날짜 수, K 합을 구하기 위한 연속적인 날짜 

arr=list(map(int,input().split()))

sum_n=0
for i in range(K): # 처음 연속되는 구간을 초기 최대 온도합으로 잡기
    sum_n+=arr[i]
max_sum=sum_n

# 처음 연속되는 구간을 제외한 만큼 반복 
# 예시)10일이면 총 9번인데 제일 처음 온도합을 제외하고 8번만 계산해서 비교
for i in range(N-K): 
    sum_n=sum_n -arr[i] + arr[i+K] # 전에 온도합구간에서 - 제일 앞에 날짜  + 겹치지 않는 다음 날짜  
    if sum_n > max_sum:
        max_sum=sum_n

print(max_sum)