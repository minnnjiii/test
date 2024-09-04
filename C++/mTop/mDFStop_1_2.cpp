#include <iostream>
#include <vector>

using namespace std;

int n; // 컴퓨터의 수 
int twin; // 컴퓨터 쌍의 수
int arr[101][101] = {0,}; // 그래프 
int visited[101] = {0,}; 
int ans = 0;

void recur(int num)
{

    if (visited[num] == 1) return;
    visited[num] = 1;
    ans += 1;
    
    for (int i = 1; i <= n; i++)
    {
        if (arr[num][i] == 1 && visited[i] == 0)
        {
            recur(i);
        }
        
    }
    
    



}

int main()
{
    cin >> n; // 컴퓨터 수 입력 받기
    cin >> twin; // 컴퓨터 쌍의 수 입력받기

    int a,b;
    for (int i = 0; i < twin; i++)
    {
        cin >> a >> b;
        arr[a][b] = 1;
        arr[b][a] = 1;  
    }
    

    recur(1);

    cout << ans -1;


}