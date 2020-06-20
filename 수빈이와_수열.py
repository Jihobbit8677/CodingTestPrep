# B수열
#
# iteration?

#B수열부터 만들어 보겠다?
# n = N
# cnt = 0
# while(cnt < n):
#
#
#     number = sum(range(:))/
#     print(number)
#     cnt += 1
#
#

#역연산
#계차수열 이미지? 평균 복원
# N, B = input(), list(map(int, input().split())) #입력을 받는 형식! 외우는게 편함ㅋㅋㅋㅋ
#
#
# An = lst[n-1]*n - lst[n-2]*(n-1)



#####안수빈 쌤 답#######
N, B = input(), list(map(int, input().split()))

A = [B[0]] #초깃값에 추가해줄게~

for i in range(1,N):
    A.append(B[i]*(i+1)-sum(A)) #i+1조심!
    #A[]=
for i in A:
    print(i, end = '')



#sol2) append가 아닌 덮어씌우기!

N, B = input(), list(map(int, input().split()))

A = [0 for i in B] #0으로 자리 미리 깔아놓는겨 ---> 후에 sum으로 할 때 지장 없도록 0으로 한겨
A[0] = B[0]

for i in range(1,N):
    A[i] = B[i]*(i+1) - sum(A) #같은 수열 내에서 계산해준것 보다 cross 계산함

for k in A:
    print(k, end='')
