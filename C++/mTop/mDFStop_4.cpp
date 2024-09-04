#include <iostream>
#include <algorithm>

using namespace std;

// DFS_top_4_럭셔리 여행

// 가장 비용이 많이 나왔을 때 비용 구하기
// 가장 비용이 적게 나왔을 때 비용 구하기


int N; // 여행지의 갯수
int s,e; // 출발 노드와 도착 노드 번호
int minSum =  21e8;
int maxSum = 0;
int visited[1001];
int graph[1001][1001] = {0,};

void recur(int now, int sum)
{
    if (now == e)
    {
        maxSum = max(sum,maxSum);
        minSum = min(sum,minSum);
        return;
    }

    for (int i = 0; i < N; i++)
    {
        if (visited[i]) continue;
        if (graph[now][i] == 0) continue;
        visited[i] = 1;
        recur(i, sum+graph[now][i]);
        visited[i] = 0;
        
        
    }
    
    
}


int main()
{
    
    cin >> N; // 여행지의 갯수

    
    // 그래프 채우기
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> graph[i][j];
        }
        
    }
    
    // 출발 노드와 도착 노드 번호
    cin >> s >> e;

    // DFS 탐색
    visited[s] = 1;
    recur(s,0);
    cout << minSum << '\n';
    cout << maxSum ;

    return 0;

}