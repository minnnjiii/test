# 알파벳 개수


S = input()

arr = [0]*26
for i in S:
    arr[ord(i)-97] += 1 # ord('a') 는 97이므로! 97을 빼 0으로 만들어줌
    # 즉 아스키 코드를 사용하여 인덱스화 한다
print(*arr)