#include <iostream>
#include <string>
using namespace std;

string player;
string angel;
string devil;
int stone_length;

// str : 플레이어 스크롤 문자 1번 index 부터 시작
// dir : 천사, 악마 돌다리 위치 1은 천사, 0은 악마
// idx : 돌다리에서 플레이어 위치 부터 시작
int dfs(int scrollIdx, int dir, int idx)
{
    if (scrollIdx == player.length())
    {
        return 1;
    }
  
  	if (idx > player.length())
    {
      return 0;
    }
    // 천사인 경우
    if (dir == 0)
    {
        for (int i = idx; i < stone_length; i++)
        {
            if (player[scrollIdx] == devil[i])
            {
                dfs(scrollIdx + 1, 1, i + 1);
            }
        }

    }
    // 악마인 경우
    else if (dir == 1)
    {
        for (int i = idx; i < stone_length; i++)
        {
            if (player[scrollIdx] == angel[i])
            {
                dfs(scrollIdx + 1, 0, i + 1);
            }
        }
    }
    
}


int main()
{
    cin >> player;
    cin >> angel;
    cin >> devil;

    stone_length = angel.length();
    int res = 0;

     res += dfs(0, 1, 0);
      
    
     res += dfs(0, 0, 0);

    cout << res;
}