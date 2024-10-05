#include <iostream>
#include <vector>
#include <string>

using namespace std;

int T; // test case
int N; // 필드의 크기 N (2 <= N <= 5)
int Q; // 조종한 횟수
int success[5]; // 성공 여부 저장 (0 또는 1)

int main() {
    
    cin >> T;
    
    for (int testcase = 0; testcase < T; testcase++)
    {
        cin >> N; // 필드의 크기
        vector<vector<char>> map(N, vector<char>(N)); // 필드 초기화
        
        int init_X = -1, init_Y = -1;
        int target_X = -1, target_Y = -1;

        cin.ignore(); // 이전 입력 후 개행문자 처리
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                scanf(" %c", &map[i][j]); // 앞에 공백 추가
                if (map[i][j] == 'X')
                {
                    init_X = i;
                    init_Y = j;
                }
                else if (map[i][j] == 'Y')
                {
                    target_X = i;
                    target_Y = j;
                }
            }
        }
        
        cin >> Q;
        for (int order = 0; order < Q; order++)
        {
            int CmdLineLength;
            cin >> CmdLineLength;

            vector<char> Cmd(CmdLineLength); // char 배열 대신 vector 사용
            cin.ignore(); // 이전 입력 후 개행문자 처리
            
            for (int length = 0; length < CmdLineLength; length++)
            {
                scanf(" %c", &Cmd[length]); // 앞에 공백 추가
            }
            
            int nowX = init_X, nowY = init_Y; // 초기 위치 설정
            int Nowdirect = 0; // 현재 보고 있는 방향
            
            for (int length = 0; length < CmdLineLength; length++)
            {
                if (Cmd[length] == 'L')
                {
                    Nowdirect = (Nowdirect + 3) % 4; // 왼쪽으로 방향 전환
                }
                else if (Cmd[length] == 'R')
                {
                    Nowdirect = (Nowdirect + 1) % 4; // 오른쪽으로 방향 전환
                }
                else if (Cmd[length] == 'A')
                {
                    // 앞으로 한 칸 이동
                    if (Nowdirect == 0 && nowX > 0 && (map[nowX - 1][nowY] == 'G' || map[nowX - 1][nowY] == 'Y' || map[nowX-1][nowY] == 'X')) // 위
                    {
                        nowX -= 1;
                    }
                    else if (Nowdirect == 1 && nowY < N - 1 && (map[nowX][nowY + 1] == 'G' || map[nowX][nowY + 1] == 'Y' || map[nowX][nowY+1] == 'X')) // 오른쪽
                    {
                        nowY += 1;
                    }
                    else if (Nowdirect == 2 && nowX < N - 1 && (map[nowX + 1][nowY] == 'G'|| map[nowX + 1][nowY] == 'Y' || map[nowX][nowY] == 'X')) // 아래
                    {
                        nowX += 1;
                    }
                    else if (Nowdirect == 3 && nowY > 0 && (map[nowX][nowY - 1] == 'G'|| map[nowX][nowY - 1] == 'Y' || map[nowX][nowY-1] == 'X')) // 왼쪽
                    {
                        nowY -= 1;
                    }
                }
            }

            // 목적지 도달 여부 확인
            success[order] = (nowX == target_X && nowY == target_Y) ? 1 : 0;
        }
        
        // 각 testcase의 커맨드마다 목적지에 도달할 수 있다면 1, 아니면 0을 공백으로 구분하여 출력함
        cout << '#' << testcase + 1 << ' ';
        for (int num = 0; num < Q; num++)
        {
            cout << success[num] << ' ';
        }
        cout << '\n';
    }
    
    return 0;
}
