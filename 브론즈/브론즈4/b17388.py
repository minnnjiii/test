# 와글와글 숭고한_17388

S, K, H = map(int,input().split())

if S + K + H < 100 : 
    if min(S,K,H) == S :
        print("Soongsil")
    elif min(S,K,H) ==  K : 
        print("Korea")
    elif min(S,K,H) == H : 
        print("Hanyang")
else : 
    print("OK")