def find_strings(myString, i, pat):
    for x in pat:
        if x != myString[i]:
            return 0
        i += 1
    return 1

def solution(myString, pat):
    if len(myString) < len(pat):
        return 0

    myString = myString.lower()
    pat = pat.lower()

    for i in range(len(myString) - len(pat) + 1):
        if find_strings(myString, i, pat):
            return 1

    return 0
