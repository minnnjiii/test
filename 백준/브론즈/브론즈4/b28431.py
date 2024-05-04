# 양말 짝 맞추기
# 28431번


sock = [] 

for i in range(5):
    num = int(input())

    if num in sock:
        sock.remove(num)
    else:
        sock.append(num)

print(sock[0])