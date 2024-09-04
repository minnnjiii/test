#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;;

    for (int i = 0; i < T; i++)
    {

        int N;
        cin >> N;

        int arr[8][8] = {0}; // N의 최댓값은 7이니까 크기는 8로 해줌
        
        // 행렬 입력 받기
        for (int j = 0; j < N; j++)
        {
            for (int k = 0; k < N; k++)
            {
                cin >> arr[j][k];
            }
            
        }

        // 행렬 90도 회전하기
        int ans90[8][8] = {0};

        for (int j = 0; j < N; j++)
        {
            for (int k = 0; k < N; k++)
            {
                ans90[k][N - 1 - j] = arr[j][k];
                
            }

        }

        
        // 행렬 180도 회전하기
        int ans180[8][8] = {0};

        for (int j = 0; j < N; j++)
        {
            for (int k = 0; k < N; k++)
            {
                ans180[k][N - 1 - j] = ans90[j][k];
            }

        }


        // 행렬 270도 회전하기
        int ans270[8][8] = {0};

        for (int j = 0; j < N; j++)
        {
            for (int k = 0; k < N; k++)
            {
                ans270[k][N - 1 - j] = ans180[j][k];
            }

        }


        
        // 출력

        cout << "#" << i +1 << "\n";

        for (int j = 0; j < N; j++)
        {
            for (int k = 0; k < N; k++)
            {
                cout << ans90[j][k];
                
            }
            cout << " ";
            
            for (int k = 0; k < N; k++)
            {
                cout << ans180[j][k];
                
            }

            cout << " ";
            
            for (int k = 0; k < N; k++)
            {
                cout << ans270[j][k];
                
            }

            cout <<"\n";


        }
        

        

    }
    


}