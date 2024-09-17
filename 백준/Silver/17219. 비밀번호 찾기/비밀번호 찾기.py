import sys
input=sys.stdin.readline

# N: 저장된 사이트 주소의 수 M: 비밀번호를 찾으려는 사이트 주소의 수
N, M=map(int,input().split())
site_dict={}
for _ in range(N):
    site, password= input().split()
    site_dict[site]=password
for _ in range(M):
    print(site_dict[input().strip()])