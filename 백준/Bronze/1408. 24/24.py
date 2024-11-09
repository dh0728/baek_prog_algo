h1, m1, s1 = map(int, input().split(':')) # 시분초를 나누기
h2, m2, s2 = map(int, input().split(':'))

t = h2*3600+m2*60+s2 - (h1*3600+m1*60+s1) # 초로 바꿔 계산후 빼

if t < 0: # 값이 음수라면
    t += 60*60*24 # 24시간어치 초를 더하기
h = t//3600 # 시간은 3600으로 나눈 몫
m = (t%3600)//60 # 분은 그 나머지를 60으로 나눈 몫
s = t%60 # 초는 그 나머지
print("%02d:%02d:%02d" % (h,m,s))