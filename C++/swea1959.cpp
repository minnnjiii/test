#include <iostream>
#include <vector>

using namespace std;


int main()
{   
    int T;
    cin >> T ;
    
    for (int k = 0; k < T; ++k)
    {
        
        // N, M 입력 받기
        int N, M;
        int N_arr[50] = {0};
        int M_arr[50] = {0};

        cin >> N >> M;


        // 배열 만들어주기
        for (int i = 0; i < N; i++) {
            cin >> N_arr[i] ; 
        }

        for (int i = 0; i < M; i++) {
            cin >> M_arr[i] ; 
        }

        // 이제 계산
        int move = abs(N - M) + 1;
        int sum, res = 0;

        if (N > M) 
        {
           for (int l = 0; l < move; l++) // 몇 번 움직일거임
            {
                for (int h = 0; h < 20; h++)
                {
                    sum += N_arr[h+l] * M_arr[h]; // N이 더 큰 경우엔 N배열 idx에 지금 몇 번 움직였는지 더해주기
                }
                if (sum > res)
                {
                    res = sum;
                }
                
                sum = 0;
            }
        }
        else
        {
            for (int l = 0; l < move; l++) // 몇 번 움직일거임
            {
                for (int h = 0; h < 20; h++)
                {
                    sum += N_arr[h] * M_arr[h+l]; 
                }
                if (sum > res)
                {
                    res = sum;
                }
                
                sum = 0;
            }
        }

        cout << "#" << k+1 << " " << res << "\n";
        
        
        









    }
    

}