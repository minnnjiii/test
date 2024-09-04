#include <iostream>

using namespace std;


int cnt = 0;
int branch;
int level;

void recur(int n){



    cnt ++;

    for (int i = 0; i < branch; i++)
    {
        recur(n + 1);
    }

    
    if (n == level)
    {
        cout << cnt;

        return;
    }

    
}

int main(){

    
    cin >> branch >> level;
    recur(cnt);

    
};