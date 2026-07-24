def solution(s):
    
    stack = []

    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack: # 비어있으면
                return False
            stack.pop()
    
    if stack: # 아직 괄호가 남아있으면
        return False
    
    return True