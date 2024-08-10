#include <iostream>

using namespace std;

// graph 순회

int N, K; // 노드의 개수 N, 간선의 개수 K
int S; // 탐색을 시작할 노드 번호 S

int graph[101][101] = {0,}; // 그래프
int visited[101] = {0,};

void preorder(int now)
{

    
    
    visited[now] = 1;
    cout << now << " ";
    
    for (int i = N; i >= 1; i--)
    {
        if (visited[i] == 1)
        {
            continue;
        }
        if (graph[now][i] == 0)
        {
            continue;
        }
        preorder(i);
        
    }
    


}

void postorder(int now)
{
    

    visited[now] = 1;
    for (int i = N; i >= 1; i--)
    {
        if (visited[i] == 1)
        {
            continue;
        }
        if (graph[now][i] == 0)
        {
            continue;
        }
        
        postorder(i);

        
    }

    cout << now << " ";
    

}


int main()
{
    

    cin >> N >> K ; // 노드의 개수 N, 간선의 개수 K 입력 받기
    cin >> S; // 탐색을 시작할 노드 번호 S 입력 받기
    
    for (int i = 0; i < K; i++)
    {
        int A,B;
        cin >> A >> B;

        graph[A][B] = 1;
    }
    
    
    preorder(S);
    fill(begin(visited),end(visited),0);
    cout << '\n';
    postorder(S);





}