#include <iostream>
#include <algorithm>
#include <vector>


using namespace std;

// DFS_top_4_럭셔리 여행

// 가장 비용이 많이 나왔을 때 비용 구하기
// 가장 비용이 적게 나왔을 때 비용 구하기

int N; // 여행지의 갯수 N
int graph[101][101] = {0,};
int visited[101] = {0,};

int minSum= 21e8;
int maxSum = 0;
int st;
int en;


void recur(int n, int sum)
{

    if (n == en)
    {
        minSum = min(sum,minSum);
        maxSum = max(sum,maxSum);
        return;
    }

    for (int i = 0; i < N; i++)
    {
        if(visited[i]) continue;
        if(graph[n][i] == 0) continue;
        visited[i] = 1;
        recur(i, sum+graph[n][i]);
        visited[i] = 0;
        
        
    }
    
    
}

int main()
{
    
    cin >> N;
    for (int from = 0; from < N; from++)
    {
        for (int to = 0; to < N; to++)
        {   
            cin >>  graph[from][to] ;

        }
    }

    cin >> st >> en;
    visited[st] = 1;
    recur(st,0);

    cout << minSum << '\n';
    cout << maxSum;

}