#include <iostream>
#include <vector>

using namespace std;


// 최단 거리가 아닌, 최소 리모컨 조작 횟수로
// 출발지에 목적지까지 ㄱㄱ

// RC카를 이동하려는데 나무가 막혀서 아빠가 그 나무 베려고 함
// 아빠가 벨 수 있는 최대 나무의 수가 주어졌을 때 
// 차윤이가 RC카를 목적지까지 이동시키기 위한
// 최소 조작 횟수는? 


// 차윤은 항상 위를 바라보는 상태로 RC카 조작 시작

int T; //test case
int N, K; //맵의 크기 N, 나무를 벨 수 있는 횟수 K
int main()
{
    cin >> T; //test case
    for (int testcase = 0; testcase < T; testcase++)
    {
        cin >> N >> K; //맵의 크기 N, 나무를 벨 수 있는 횟수 K
        vector<vector<char>> map(N, vector<char>(N)); // 맵 초기화
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                scanf(" %c", &map[i][j]); // 앞에 공백 추가
            }
            
        }
        
        


        cout << '#' << testcase + 1 << ' ' << '\n';
    }
}