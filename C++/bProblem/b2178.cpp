#include <bits/stdc++.h>
using namespace std;

// 1,1에서 N,M의 위치까지 이동할 때 지나야 하는 최소의 칸 수 구하기   
// 백준/2178 미로게임

// 문제에서 주어진 맵은 한 칸 한 칸 이동함
// 가중치가 같은 맵에서 최단거리로 사용할 수 있는 BFS 사용

const int max_n = 104; 

// 상하좌우 방향
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1}; 

// n : 미로의 세로 크기,  m : 미로의 가로 크기
// a배열 : 미로의 맵을 저장함
// visitied 배열 : 각 칸의 방문 여부와 거리를 저장함
int n, m, a[max_n][max_n], visited[max_n][max_n], y, x; 

int main(){ 


    // 미로 크기 n*m 입력 받기
    scanf("%d %d", &n, &m); 

    // 미로 입력받기
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            scanf("%1d", &a[i][j]);
        }
    } 

    // 두 변수를 저장할 수 있게 pair<int,int> 사용
    queue<pair<int, int>> q;  

    // 시작 위치 0,0은 방문한 것으로 표시하며 거리는 1로 설정
    visited[0][0] = 1;

    // 시작 위치를 큐에 추가함
    q.push({0, 0});  

    // q에 담긴 좌표를 하나씩 꺼내보면서 탐색하는데,
    // q에서 모두 꺼내고 비게 되었다면 탐색을 마침
    while(q.size()){
        tie(y, x) = q.front(); q.pop();  // 큐에서 좌표를 꺼내고 y, x에 저장함
        // 상하좌우 네 방향 탐색
        for(int i = 0; i < 4; i++){
            // 새로운 위치 계산
            int ny = y + dy[i]; 
            int nx = x + dx[i]; 

            if(ny < 0 || ny >= n || nx < 0 || nx >= m || a[ny][nx] == 0) continue;  // 맵 벗어나면 넘겨
            if(visited[ny][nx]) continue; // 방문했어도 넘겨

            // 새로운 위치의 거리 = 현재 위치 거리 + 1
            visited[ny][nx] = visited[y][x] + 1;

            // 큐에 다음 좌표를 넣어서 BFS 계속함
            q.push({ny, nx}); 
        } 
    }

    // 미로의 끝 위치 출력
    printf("%d", visited[n - 1][m - 1]); 
    return 0;
}  

