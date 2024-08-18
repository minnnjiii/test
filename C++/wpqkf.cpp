#include <iostream>
#include <algorithm>
#include <vector>
#include <climits>

using namespace std;

int T; // test case의 개수
int N; // 나무의 개수
vector<int> arr; 
int maxTreeLen = 0; // 제일 큰 나무의 길이
int answer = INT_MAX;

// now = 현재 나무 길이 
// oddDays = 홀수 날 물을 준 횟수
// evenDays = 짝수 날 물을 준 횟수
// ans = 현재까지의 날짜 수
// idx = 현재 처리 중인 나무의 인덱스
// isOddDay = 현재가 홀수 날인지 짝수 날인지

void recur(int now, int oddDays, int evenDays, int ans, int idx, bool isOddDay)
{
    now = arr[idx] + oddDays + evenDays * 2;

     if ( now == maxTreeLen) // 모든 나무에 대한 처리가 끝난 경우
    {
        if (idx == N-1)
        {
            answer = min(ans,answer);
            return;
        }
        else recur(0,0,0,ans,idx+1,true);
    
    }


    if (now > maxTreeLen) return;
    

    if (isOddDay) // 현재가 홀수 날인 경우
    {
        recur(now, oddDays + 1, evenDays, ans + 1, idx, false); // 짝수 날로 넘어가기
    }
    else // 현재가 짝수 날인 경우
    {
        recur(now, oddDays, evenDays + 1, ans + 1, idx, true); // 다음 홀수 날로 넘어가기
    }

    // 마법의 물뿌리개를 사용하지 않고 날짜를 넘기는 경우도 고려
    recur(now, oddDays, evenDays, ans + 1, idx, !isOddDay); // 홀수->짝수 또는 짝수->홀수로 넘어감
}

int main()
{
    cin >> T; // test case 입력 받기
    for (int j = 0; j < T; j++) // test case만큼 나무 입력 받고 출력할거임
    {
        cin >> N; // 나무 개수 입력 받기
        arr.resize(N); // 배열 사이즈 재조정해주기

        maxTreeLen = 0; // 제일 큰 나무의 길이
        answer = INT_MAX;
        
        for (int i = 0; i < N; i++) // 나무 개수만큼 arr 배열에 나무 크기 입력해주기
        {   
            cin >> arr[i];
            maxTreeLen = max(arr[i], maxTreeLen);
        }

        recur(0, 0, 0, 0, 0, true); // 첫날은 홀수날로 시작
        cout << '#' << j + 1 << ' ' << answer << '\n';
    }
}
