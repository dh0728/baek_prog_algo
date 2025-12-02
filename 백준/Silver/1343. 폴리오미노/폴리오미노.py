import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

board = input()

idx = 0
newboard = []
while idx<len(board):
    if board[idx:idx+4]=='XXXX':
        newboard.append('AAAA')
        idx += 4
    elif board[idx:idx+2]=='XX':
        newboard.append('BB')
        idx += 2
    elif board[idx]=='X':
        newboard = ['-1']
        break
    else :
        newboard.append(board[idx])
        idx += 1

print(''.join(newboard))