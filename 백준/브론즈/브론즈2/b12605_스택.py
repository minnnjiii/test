# 백준/12605번
# 단어순서 뒤집기

for i in range(int(input())):
    n = input().split()
    print(f"Case #{i+1}: {' '.join(n[::-1])}")