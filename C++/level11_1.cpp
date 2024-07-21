#include <iostream>

using namespace std;

int main(){

    bool flag = false;

    int arr[7] = {3,4,1,3,2,7,3};
    int n;

    cin >> n;
    
    for (int i = 0; i < 7; i++)
    {
        if (arr[i] == n)
        {
            flag = true;
        }
        
    }
    
    if (flag)
    {
       cout << "발견";
    }
    else cout << "미발견";




}