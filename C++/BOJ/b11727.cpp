#include <iostream>
#include <vector>

using namespace std;


int n;

int recur(int N)
{
    vector<int> graph(N + 1);
    graph[0] = 1;
    graph[1] = 1;

    for (int i = 2; i <= N; ++i)
        graph[i] = (graph[i - 1] + 2 * graph[i - 2]) %10007;

    return graph[N];
}
int main()
{
    cin >> n;
    cout << recur(n);
    return 0;
}