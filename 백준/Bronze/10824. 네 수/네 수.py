str_list=input()
str_list=str_list.split()
num_list = list(map(int, str_list))

num = num_list[0]
num2 = num_list[1]
AB = int(str(num)+str(num2)) 

num = num_list[2]
num2 = num_list[3]
CD = int(str(num)+str(num2))

print(AB+CD)