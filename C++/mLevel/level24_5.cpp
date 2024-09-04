#include <iostream>
#include <string>

using namespace std;
int main()
{
    string ss[5];
    
    for (int i = 0; i < 5; i++)
    {
        string s;
        cin >> s;
        ss[i] = s;
    }
    int cnt = 0;
    
    for (int i = 0; i < 5; i++)
    {
        
        // MCD가 여러번 등장하는 경우도 계산해줘야해서 while문으로 계산해줌
        size_t pos = ss[i].find("MCD");
        while (pos != string::npos) {
            cnt++;
            pos = ss[i].find("MCD", pos + 1); // 다음 "MCD" 찾기
        }
        
    }
    cout << cnt;


}