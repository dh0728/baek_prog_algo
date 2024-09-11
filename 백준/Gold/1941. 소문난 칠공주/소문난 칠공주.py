def dfs(depth,coords,Y_cnt,S_cnt):
    global cnt
    if Y_cnt >= 4:
        return
    if depth==7:
        coords.sort()
        new_coords = tuple(coords)
        # print(new_coords)
        if new_coords not in can_set:
            cnt+=1
            can_set.add(new_coords)
        return

    for coord in coords:
        x,y= coord[0], coord[1]
        for dx, dy in dxy:
            ni = x + dx
            nj = y + dy
            if ni < 0 or ni >= 5 or nj < 0 or nj >= 5:
                continue
            if (ni,nj) in coords:
                continue
            if arr[ni][nj] == 'Y':
                dfs(depth+1,coords+[(ni,nj)],Y_cnt+1,S_cnt)
            else:
                dfs(depth+1,coords+[(ni,nj)],Y_cnt,S_cnt+1)

arr=[list(input()) for _ in range(5)]
cnt=0
can_set=set()

dxy=[[0,1],[1,0],[0,-1],[-1,0]]
for i in range(5):
    for j in range(5):
        if arr[i][j]=='Y':
            dfs(1,[(i, j)], 1, 0) # 시작좌표, Y_cnt, S_cnt
        else:
            dfs(1,[(i, j)], 0, 1)
# print(can_set)
print(cnt)