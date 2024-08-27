
#include <iostream>
#include <algorithm>

using namespace std;


// swea_4012_요리사


// 맛의 차이가 최소가 될 때의 그 차이값 구하는 문제 

int T; // test case
int N, ans; // 식재료의 수 

int arr[17][17]; 
bool visited[17]; 

void recur(int idx, int depth)
{

    if ( depth == N/2 )
    { 
        int A = 0;
        int B = 0;

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (visited[i] && visited[j])
                    A += arr[i][j];
                else if (!visited[i] && !visited[j])
                    B += arr[i][j];
            }
        }
        ans = min(ans, abs(A-B));
        return;
    }

        if (idx >= N || ans == 0)
            return;

        visited[idx] = false;
        recur(idx + 1, depth);
        visited[idx] = true;
        recur(idx + 1, depth + 1);

}

int main()
{
    
    cin >> T; // test case 입력 받기

    for (int k = 0; k < T; k++)
    {

        cin >> N; // 식재료의 수 입력 받기
        ans = 21e8; // test case 마다 ans를 초기화 해줘야하므로 이렇게 test case 안에다 넣어줌
        
        // 식재료들의 시너지 배열 arr 입력 받기
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                cin >> arr[i][j];
            }
        }


        // DFS 시작 👀
        recur(0,0);

        cout << '#' << k+ 1 << ' ' << ans << '\n';
    }



}