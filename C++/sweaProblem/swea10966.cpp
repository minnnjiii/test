#include <iostream>
#include <queue>
#include <cstring>
using namespace std;



// 물이면 'W', 땅이면 'L'로 표현됨
// 땅으로 표현된 모든 칸에 대해서, 
// 어떤 물인 칸으로 이동하기 위한 최소 이동 횟수를 구하고 
// 모든 이동 횟수의 합을 출력하는 문제

// swea_10966_물놀이를 가자

int N, M; // N * M 크기의 맵
int map[1000][1000];
int visited[1000]; 
int ans;
int dirr[] = { 1,-1,0,0 };
int dirc[] = { 0,0,1,-1 };

struct node
{
    int x;
    int y;
};

int main()
{

    int T; // test case
    cin >> T;
    for (int testcase = 0; testcase < T; testcase++)
    {

        // N * M 크기의 맵을 입력받기 -----------------
        cin >> N >> M;
        
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                cin >> map[i][j];
            }
        }

        // ---------------------------------------

        queue<node> q;
        memset(map,-1,sizeof(map));

        for (int i = 0; i < N; i++)
        {
            string temp; 
            cin >> temp;
            for (int j = 0; j < M; j++) 
            {
                if (temp[j] == 'W')
                {
                    q.push({ i,j });
                    map[i][j] = 0;
                }                                
            }
        }
        ans = 0;
        while (!q.empty())
        {
            int row = q.front().x;
            int col = q.front().y;
            q.pop();
            for (int dir = 0; dir < 4; dir++)
            {
                int nrow = row + dirr[dir];
                int ncol = col + dirc[dir];
                if (nrow < 0 || ncol < 0 || nrow >= N || ncol >= M) continue;
                if (map[nrow][ncol] >= 0) continue;                              
                map[nrow][ncol] = map[row][col] + 1;
                ans += map[nrow][ncol];
                q.push({ nrow,ncol });                
            }
        
        }

        cout << '#' << testcase + 1 << ' ' << ans << '\n';
    }


}
