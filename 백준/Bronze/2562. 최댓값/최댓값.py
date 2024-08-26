arr=[[int(input()),i] for i in range(1,10)] # [값,값번호] 형태로 리스트 생성

for i in range(1,len(arr)): # index 0 과 나머지 차례로 비교해 제일 큰값 찾기
    if arr[0][0] < arr[i][0]:
        arr[0], arr[i] = arr[i], arr[0]
print(f'{arr[0][0] }\n{arr[0][1]}')