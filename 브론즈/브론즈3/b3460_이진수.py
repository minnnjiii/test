# 이진수
# 3460번 

n = int(input()) # test case 갯수 


for i in range(n) : 
    
    num = int(input())
    binary = 0 

    while num > 0 : 
        if num % 2 == 1 : 
            print(binary, end = ' ')
        num = num // 2 
        binary += 1 


    

'''

13을 2진수로 바꾸기 

2)13
ㅡㅡㅡ
2) 6 .. 1 
2 ) 3 .. 0
2 ) 1 .. 1 

즉 1101 이 13의 이진수다. 

숫자를 이진수로 표현할 때 가장 오른쪽 비트부터 차례대로 0부터 
번호를 매기는 것이 일반적이다. 

따라서 십진수 13을 이진수로 변환하면 1101이 되고 
1101에 번호를 매기면 아래와 같다.

1 1 0 1 
3 2 1 0 



'''