#include <iostream>
#include <algorithm>

using namespace std;

// swea_1952_수영장
// 12개월 이용 계획대로 수영장을 이용하는 경우 중 가장 적게 지출하는 비용을 구하는 문제
// 1일, 1달, 3달, 1년

// 1일 이용권으로만 이용했을 때의 가격으로 먼저 구성해
// 그 다음에 한 달 이용권을 생각하는데 1일 이용권보다 한 달 이용권이 더 저렴하면 한달 이용권 가격으로 ㄱㄱ
// 3달 이용권은 모든 경우의 수를 다 계산해주기

int T; // test case
int daysPrice, monthPrice, threeMonthPrice, yearPrice; // 1일 이용권의 요금, 1달 이용권의 요금, 3달 이용권의 요금, 1년 이용권의 요금
int plan[12];
int ans;


void recur(int idx){

    


}



int main()
{
    
    cin >> T; // test case
    for (int testcase = 0; testcase < T; testcase++)
    {    
        ans = 0;
        memset(plan, 0, sizeof(plan));
        cin >> daysPrice >> monthPrice >> threeMonthPrice >> yearPrice;  // 1일 이용권의 요금, 1달 이용권의 요금, 3달 이용권의 요금, 1년 이용권의 요금
        
        // 12개월 이용 계획 받기
        for (int k = 0; k < 12; k++)
        {
            cin >> plan[k];
        }
        
        
        // 1일 이용권으로만 구성했을 때와 한 달 이용권으로만 구성했을 때의 
        // 가격을 비교했을 때 더 저렴한 가격을 ans에 더 해주기
        // 왜냐?? 우리는 최소 비용을 찾고 있으니까! 
        for (int i = 0; i < 12; i++)
        {
            int t = plan[i] * daysPrice;
            if (t < monthPrice)
            {
                ans += t;
            }
            else
            {
                ans += monthPrice;
            }
        }


        // recur부르기 



        if (ans > yearPrice)
        {
            ans = yearPrice;
        }


        // 정답 출력
        cout << '#' << testcase + 1 << ' ' << ans << '\n';
    }



}