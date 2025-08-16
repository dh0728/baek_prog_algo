
def solution(myStr):
    answer = []
    
    idx = 0
    for i in range(len(myStr)):
        if (myStr[i] == 'a' or myStr[i] == 'b' or myStr[i] == 'c'):
            if (myStr[idx:i] !=""):
                answer.append(myStr[idx:i])
            idx = i+1
        
    if (myStr[idx: len(myStr)] != "" and idx < len(myStr) ):
        answer.append(myStr[idx:len(myStr)])
    
    if len(answer) == 0:
        answer.append("EMPTY")
    return answer