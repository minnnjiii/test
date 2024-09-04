#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// DFS_top_5_해밀턴 회로
// 1번 정점에서 출발하여 모든 정점을 들린 후, 다시 1번 정점으로 돌아오는 최소 비용 출력하기


int N; // 정점의 수
int graph[14][14] = {0,};
int visited[14] = {0,};


int ans = 999;

void recur(int now, int price, int cnt)
{
    
    if (cnt == N-1)
    {
        ans = min(price,ans);
    }
    

    for (int i = 0; i < N+1; i++)
    {
        if (visited[i] == 1) continue;
        if (graph[now][i] == 0) continue;

        visited[i] = 1;
        recur(i,price+graph[now][i],cnt+1);


    }
    
    

}



int main()
{
    int x;
    cin >> N;
    for (int i = 1; i < N+1; i++)
    {
        for (int j = 1; j < N+1; j++)
        {
            cin >> x;
            graph[i][j] = x;
        }
    }

    recur(1,0,1);
    
    cout << ans;

}