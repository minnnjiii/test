#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


// 🍙 문제 
// N개의 나무 정보가 주어졌을 때,
// 모든 나무의 크기가 초기의 키가 가장 컸던 나무와
// 같아지도록 만들기 위한 <<<<<최소 날짜 수>>>>>>를 계산하는 문제 

// 홀수 번째 날에 물을 준 나무는 키가 1️⃣만큼 자라고(1 만큼 자라고)
// 짝수 번째 날에 물을 준 나무는 키가 2️⃣만큼 자람. (2 만큼 자람)
// 어떤 날에는 마법의 물뿌리개를 사용하지 않을 수도 있음

int T; // test case의 개수
int N; // 나무의 개수
vector<int> arr; 
int maxTreeLen = 0; // 제일 큰 나무의 길이
int answer = 21e8;
int visited[101];

// now = 현재 나무 길이 
// ans = 며칠 걸렸는지, 나무 자라는데 며칠 걸렸는지 확인하기 위한 변수임
// idx = 4개의 나무가 있으면 4개 다 최고 길이가 될때까지 검사해야하잖아. 그 4개를 다 돌았는지 확인하기 위한 idx변수임
// cnt = 얘가 첫째날을 거쳤는지 확인하기 위한 변수임. 첫째날 거치지 않고 바로 둘째날 가는 경우를 제외하기 위함
void recur(int now, int oddDays, int evenDays, int ans, int idx)
{
    
    // visited 부분...
    if (visited[idx-1] && visited[idx-1] == 0)
    {
        return;
    }
    
    now = arr[idx] + oddDays + evenDays*2;

    if ( now == maxTreeLen) // 모든 나무에 대한 처리가 끝난 경우
    {
        if (idx == N-1)
        {
            answer = min(ans,answer);
            return;
        }
        else recur(0,0,0,ans,idx+1);
    
    }

    if (now > maxTreeLen) return;
    
    // visited 부분...
    visited[idx] = 1;
    recur(now, oddDays+1, evenDays, ans +1,idx);
    recur(now, oddDays, evenDays +1 , ans +1,idx);
    visited[idx] = 0; // visited 부분...

}



int main()
{
    cin >> T; // test case 입력 받기
    for (int j = 0; j < T; j++) // test case만큼 나무 입력 받고 출력할거임
    {
        cin >> N; // 나무 개수 입력 받기
        arr.resize(N); // 배열 사이즈 재조정해주기

        maxTreeLen = 0; // 제일 큰 나무의 길이
        answer = 21e8;
        
        for (int i = 0; i < N; i++) // 나무 개수만큼 arr 배열에 나무 크기 입력해주기
        {   
            cin >> arr[i]; // arr배열에 나무 크기가 하나씩 들어가는 중! ^__^ 
            maxTreeLen = max(arr[i], maxTreeLen);
        
        }

        recur(0,0,0,0,0);
        cout << '#' << j+1 << ' ' << answer << '\n';

    }
    
}