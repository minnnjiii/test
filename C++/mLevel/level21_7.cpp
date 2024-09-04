#include <iostream>

using namespace std;

void recur(int n){

    
    
    cout << n << " ";
    if (n == 1)
    {
        return;
    }
    recur(n -1);
    
    cout << n << " ";

}

int main(){

    string w;
    cin >> w;

    recur(w.size());

    

}