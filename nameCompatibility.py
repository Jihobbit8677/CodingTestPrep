
N, M = input().upper(), input().upper()

if (2 <= len(N) and len(M) <= 100):
    pass
else:
    print('이름은 2자이상 100자 이하로 적으셔야 합니다')

name1_lst = []
for (i in N):
    name1_lst.append(i)
name2_las = []
for (j in M):
    name2_las.append(j)

map(print, name1_lst, name2_lst)
