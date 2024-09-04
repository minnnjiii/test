#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int arr[11][11];
int mask[11][11];
int DAT[10] = {0};

struct Datas
{
    int value;
    int cnt;
};



bool compare(Datas a, Datas b){

    if (a.cnt == b.cnt)
    {
        return a.value < b.value;
    }
    return a.cnt > b.cnt;

}

int main(){

    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> arr[i][j];
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> mask[i][j];
        }
    }
    
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (mask[i][j] == 1)
            {
                DAT[arr[i][j]]++;
            }
        }
        
    }

    vector<Datas> datas;

    for (int i = 0; i < 10; i++)
    {
        if (DAT[i]>0)
        {
            datas.push_back( {i, DAT[i]});
            
        }
    }
    
    sort(datas.begin(),datas.end(),compare);

    for (int i = 0; i < datas.size(); i++)
    {
        for (int j = 0; j < datas[i].cnt; j++)
        {
            cout<<datas[i].value<<" ";
        }
    }
    

}