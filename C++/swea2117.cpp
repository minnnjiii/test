#include <iostream>
#include <cstring>
using namespace std;

// swea_2117_홈 방범 서비스

// N*N 크기의 도시에 홍방범 서비스를 제공하려고 함
// 홍방범 서비스는 마름모 모양의 영역에서만 제공됨
// 영역의 크기 1 = 비용 1
// 회사가 손해를 보지 않으면서 홈방범 서비스를 가장 많은 집들에 제공하는 서비스 영역을 찾았을 때,
// 그 때의 서비스를 제공 받는 집들의 수임

int T; // test case
int N; // 도시의 크기 N
int M; // 하나의 집이 지불할 수 있는 비용
int map[20][20]; // 도시 map
int ans; // 정답 
int cost; //운영비용
int c,cnt;

int main()
{

    cin >> T; // test case

    for (int testcase = 0; testcase < T; testcase++)
    {   
        cin >> N >> M; // 도시의 크기 N과 하나의 집이 지불할 수 있는 비용 M 입력받기
        memset(map,0,sizeof(map));
        // 도시 정보 입력 받기
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                cin >> map[i][j];
            }

        }

        ans = 0;
        for (int k = 0; k < N+1; k++)
        {
            cost = k * k + (k+1) * (k+1);

            for (int i = 0; i < N; i++)
            {
                for (int j = 0; j < N; j++)
                {
                    c = 0;
                    cnt = 0;
                    for (int a = i-k; a <= i+k; a++)
                    {
                        for (int b = j-c; b <= j+c; b++)
                        {
                            if (a < 0 || a >= N || b < 0 || b>= N) continue;
                            if (map[a][b]) cnt ++;
                        }
                        if (a <i) c++;
                        else c--;
                        
                        
                    }
                    if (cnt * M - cost >= 0 && ans < cnt) ans = cnt;
                    
                }
                
            }
            




        }
        















        cout << '#' << testcase + 1 << ' ' << ans << '\n';

    }

}