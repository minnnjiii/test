#include <iostream>

using namespace std;

// DFS_top_5_해밀턴 회로
// 1번 정점에서 출발하여 모든 정점을 들린 후, 다시 1번 정점으로 돌아오는 최소 비용 출력하기

int N; // 정점의 수 N
int graph[13][13]; 
int visited[13] = {0,};
int mini = 21e8; // 최소비용을 의미하는 변수
bool firstFlag = true; // 맨 처음 cur은 무조건 1이므로 첫 진행을 통과시키기 위해 Firstflag = true 설정

void dfs(int cur, int dis, int cnt)
{
    if (dis > mini) return; // distance가 최소비용보다 크다면 return
    if (cur == 1 && firstFlag == false) // 첫 노드에 도달했고 
    {
        if (cnt == N) // 모든 노드를 방문했다면
        {
            if (dis < mini) 
            {mini = dis;} // mini 최소 비용 계산해준 뒤 return
            return; 
        }
        else return;
        
    }

    firstFlag = false; // 우리가 첫 진행을 통과하기 위해 firstFlag를 true로 줬음. 통과했으니까 그 이후로 쭉 False로 설정되어 있음. 

    for (int i = 1; i <= 12; i++)
    {
        if (visited[i]) continue; // 이미 방문했다면 continue
        if (graph[cur][i] == 0) continue; // 방문 불가능하다면 continue
        visited[i] = 1;
        dfs(i, dis + graph[cur][i], cnt+ 1); // 재귀를 진행하며 dis와 cnt를 올려주기
        visited[i] = 0;
        
    }
    
    
}

int main()
{

    cin >> N; // 정점의 수 N 입력받기 (1 <= N <= 12)

    // 행렬 채우기 (N * N 행렬)
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            cin >> graph[i][j];
        }
        
    }

    // 첫 노드에서 출발해 다시 첫 노드로 돌아와야 하므로 visited를 체크하지 않고 출발
    // 0번 노드는 존재하지 않음. 1번부터 출발
    dfs(1,0,0); 
    
    // 최소비용 출력
    cout << mini;
    return 0;

}