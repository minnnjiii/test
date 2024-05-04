# 별 찍기 - 15
# 10990 


'''

   *
  * *
 *   *
*     *

'''

n = int(input()) 

if n == 1 :
    print("*")

else : 
    print(" "*(n-1) + "*")
    for i in range(n,1,-1) :
        print(" "*(i-2) + "* " + " "*2*(n-i) + "*")

