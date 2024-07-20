#include <iostream>
#include <cctype>
#include <algorithm>

using namespace std;

char word;
char arr[2][3] = {
    {'F','E','W'},
    {'D','C','A'}
};


void findCh(char target){
    
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (arr[i][j] == target){
                cout << "발견";
            }
        }
        
    }cout << "미발견";



    

};


int main(){

    
    cin >> word;

    findCh(word);


}