def cal_balance(sentence):
    stack=[] # 스택 리스트 생성
    for a in sentence:
        if a=='(': # 열린 소 괄호 만나면 스택에 삽입
            stack.append(a)
        elif a==')':
            if not stack or stack[-1] != '(': # stack이 비었거나 마지막 값이 열린 소괄호가 아니면
                return  'NO'
            else: # 열린 소괄호 맞으면 마지막값 빼기
                stack.pop()

    if not stack: # for문이 끝나고 stack이 비어있어야 균형잡힌 것
        return 'YES'
    else:
        return 'NO'

N=int(input())
for _ in range(N):
    result=cal_balance(input())
    print(result)