#include <iostream>
#include <map>

using namespace std;

// DFS_top_3_크리스마스 트리

int N;


struct Node
{
    int left;
    int right;
};

map<int,Node> m;

void preorder(int now)
{
    if (now == 0)
    {
        return;
    }
    
    cout << now << " ";
    preorder(m[now].left);
    preorder(m[now].right);
    
}

void inorder(int now)
{
    if (now == 0)
    {
        return;
    }
    inorder(m[now].left);
    cout << now << " ";
    inorder(m[now].right);
        
    
}

void postorder(int now)
{
    if (now == 0)
    {
        return;
    }
    postorder(m[now].left);
    postorder(m[now].right);
    
    cout << now << " ";
}



int main()
{

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        int x,y,z;
        cin >> x >> y >> z;
        if (y != -1)
        {
            m[x].left = y;
        }
        if (z != -1)
        {
            m[x].right = z;
        }
        
        
    }



    inorder(1);
    cout << '\n';
    
    preorder(1);
    cout << '\n';


    postorder(1);
}