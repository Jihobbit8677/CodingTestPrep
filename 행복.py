def happy(Nscores):
    lst = list(scores).sort
# 입력 형태를 고려 안한 것!

N = 4
scores = 12, 12, 23, 34 #Tuple임! ---> list로!
# score_list = []
# score_list.append(list(scores).split(','))
score_list = sorted(list(scores))
score_gap = score_list[N-1] - score_list[0] #N-1놓칠뻔 했음!
print(score_gap)



######안수빈 쌤 답#######
N, lst = input(), list(map(int, input().split())) # 이눗 스플릿 해준것을 각각 인트로 매핑하고, list로 바꿔줬다.

score_gap = max(lst) - min(lst)
print(score_gap)
