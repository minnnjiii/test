#include <iostream>
using namespace std;

int n;
int arr[13][13];
int visited[13];
int minVal = 9999999;
bool firstFlag = true;

void dfs(int cur, int dis, int cnt)
{
    if (dis > minVal)
    {
        return;
    }
    if (cur == 1 && firstFlag == false)
    {
        if (cnt == n)
        {
            if (dis < minVal)
            {
                minVal = dis;
            }
            return;
        }
        else
        {
            return;
        }
    }

    firstFlag = false;

    for (int i = 1; i <= 12; i++)
    {
        if (visited[i])
        {
            continue;
        }
        if (arr[cur][i] == 0)
        {
            continue;
        }
        visited[i] = 1;
        dfs(i, dis + arr[cur][i], cnt + 1);
        visited[i] = 0;
    }
}

int main()
{
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            cin >> arr[i][j];
        }
    }

    dfs(1, 0, 0);

    cout << minVal;
    return 0;
}


