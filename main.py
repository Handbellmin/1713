import sys

input = sys.stdin.readline

n = int(input())
n1 = int(input())
answer = [0 for _ in range(n)]
satis = [0 for _ in range(n)]
ls = list(map(int, input().split(' ')))
size = 0
chk_1 = False
for i in range(n1):
  for j in range(n):
    if answer[j] == ls[i]:
      satis[j] += 1
      break
    elif answer[j] == 0:
      answer[j] = ls[i]
      break
  if answer.count(0) == 0:
    l = i
    break
  if i == n1 - 1:
    chk_1 = True
if not chk_1:
  for i in range(l + 1, n1):
    chk = False
    for j in range(n):
      if answer[j] == ls[i]:
        satis[j] += 1
        chk = True
        break
    if not chk:
      for s in range(n):
        if satis[s] == min(satis):
          answer.pop(s)
          answer.append(ls[i])
          satis.pop(s)
          satis.append(0)
          break

answer = list(set(answer))
answer.sort()
for i in range(len(answer)):
  if answer[i] != 0:
    print(answer[i], end=' ')
