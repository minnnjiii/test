# 컵홀더
# 2810번 

n = int(input()) 

seat = input()
seat = seat.replace('LL','S')

print(min((len(seat)+1),n))