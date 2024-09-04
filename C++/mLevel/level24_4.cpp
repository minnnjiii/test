#include <iostream>
#include <string>

using namespace std;
int main()
{
    string input;
    cin >> input;

    int arr[11] = {0};
    
    for (char w : input)
    {
        if (w >= 'A' && w <= 'K')
        {
            arr[w-'A']++;
        }
    }

    int maxCnt = 0;
    char maxW = 'A';
    int minCnt = 21e8;
    char minW = 'A';
    
    for (int i = 0; i < 11; i++)
    {
        if (maxCnt < arr[i])
        {
            maxCnt = arr[i];
            maxW = 'A' + i;
        }
        if (minCnt > arr[i])
        {
            minCnt = arr[i];
            minW = 'A' + i;
        }
        
        
    }
    

    cout << maxW << '\n' <<  minW;
    

}