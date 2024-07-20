#include <iostream>

using namespace std;

int main()
{
    int T; 
    cin >> T;

    for (int Testcase = 0; Testcase < T; Testcase++)
    {
        
        int N, M;
        cin >> N >> M;

        int arr[16][16] = {0};

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                cin >> arr[i][j] ;
            }
            
        }

        int max_flies = 0;
        // + shape
        for (int i = 0; i < N; ++i)
        {
            for (int j = 0; j < N; ++j)
            {
                int flies = arr[i][j];

                for (int k = 0; k < M; ++k)
                {
                    if (i + k < M) flies += arr[i + k][j]; //하
                    if(i-k >= 0) flies += arr[i-k][j]; //상
                    if (j+k < N) flies += arr[i][j+k]; //우
                    if(j-k >= 0) flies += arr[i][j-k]; //좌
                
                if (flies > max_flies)
                {
                    max_flies = flies;
                }
                
                
                }
                

            }

            for (int i = 0; i < N; ++i)
            {
                for (int j = 0; j < N; ++j)
                {
                   int flies = arr[i][j];

                   for (int k = 1; k < M; k++)
                   {
                        if (i+k < N && j +k < N) flies += arr[i+k][j+k]; 
                        if (i+k < N && j -k >= 0) flies += arr[i+k][j-k]; 
                        if (i-k >=0  && j +k < N) flies += arr[i-k][j+k]; 
                        if (i-k >=0  && j -k >= 0) flies += arr[i-k][j-k]; 
                        
                   }

                   if (flies > max_flies)
                    {
                        max_flies = flies;
                    }

                   
                   
                }
                
            }
            
            
        }
                

    cout << max_flies;

        

    }
//     N=2일때
//     arr[0][0]+arr[0][2]+arr[1][1]+arr[2][0]+arr[2][2] 
//     arr[0][1]+arr[0][3]+arr[2][2]+arr[2][1]+arr[2][3]
// ??????????????????
//     N=3일때
//     arr[0][0]+arr[0][4]+arr[1][1]+arr[1][3]+arr[2][2]+arr[3][1]+arr[3][3]+arr[4][0]+arr[4][4]

}