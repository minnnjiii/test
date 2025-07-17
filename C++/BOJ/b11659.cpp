#include <iostream>
#include <vector>

using namespace std;


int main()
{
    ios::sync_with_stdio(false); // 입출력 속도 향상
    cin.tie(0);  // cin과 cout 분리
    
    int N, M; // 수의 개수 N과 합을 구해야 하는 횟수 M
    cin >> N >> M;

    vector<int> graph(N + 1); // 입력 수 저장 
    vector<int> prefix(N + 1, 0); // 누적합

    for (int num = 1; num <= N; num++)
    {
        cin >> graph[num];
        prefix[num] = prefix[num - 1] + graph[num];
    }

    for (int k = 0; k < M;k++){
        int i, j;
        cin >> i >> j;
        cout << (prefix[j] - prefix[i - 1]) << '\n';
    }
    return 0;
}
