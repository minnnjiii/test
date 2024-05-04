#AFC윔블던_4299번

plus,minus = map(int,input().split())
ans = []

for i in range(0,plus+1):
    for j in range(0,plus+1):
        if i + j == plus and i - j == abs(minus):
            ans.append(i)
            ans.append(j)
 

if ans:  # ans가 비어있지 않은 경우에만 출력
    print(ans[0], ans[1])
else:
    print("-1")
