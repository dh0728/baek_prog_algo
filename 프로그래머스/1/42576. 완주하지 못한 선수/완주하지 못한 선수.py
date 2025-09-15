def solution(participant, completion):
    
    part_dir = {}
    
    for p in participant:
        if p in part_dir:
            part_dir[p] += 1
        else:
            part_dir[p] = 1
            
    for c in completion:
        part_dir[c] -= 1
    
    for k, v in part_dir.items():
        if v == 1:
            return k
    