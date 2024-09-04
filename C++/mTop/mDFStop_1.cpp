#include <iostream>
#include <vector>

using namespace std;

int T, twin;
int ans = 0;
vector<int> arr[101];
int visited[101] = {0,};


void recur(int n)
{
    
    if (visited[n])
    {
        return;
    }
    

    visited[n] = 1;
    ans += 1;

    for (int i = 0; i < arr[n].size(); i++)
    {
        recur(arr[n][i]);
    }
    
    
    

}

int main()
{
    
    cin >> T; // 컴퓨터의 수 입력받기
    cin >> twin; // 컴퓨터 쌍의 수 입력받기
    
    for (int i = 0; i < twin; i++)
    {
        int a, b;
        cin >> a >> b;

        arr[a].push_back(b);
        arr[b].push_back(a);

    }
    
    recur(1);
    cout << ans -1;


}