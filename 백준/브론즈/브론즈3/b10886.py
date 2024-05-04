# 0 = not cute / 1 = cute

survey = []
n = int(input())
for i in range(n):
    survey.append(int(input()))

if survey.count(1) > survey.count(0) : 
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")