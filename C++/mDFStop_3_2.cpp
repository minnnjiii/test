#include <iostream>
#include <map>

using namespace std;

// DFS_top_3_크리스마스 트리

struct star
{
    int left;
    int right;
};

map<int,star> tree;
int N;

void preorder(int now)
{
    


    if (now == -1)
    {
       return;
    }
    

    cout << now << ' ';
    preorder(tree[now].left);
    preorder(tree[now].right);
    

}



void inorder(int now)
{


    if (now == -1)
    {
       return;
    }
    

    inorder(tree[now].left);
    cout << now << ' ';
    inorder(tree[now].right);
}


void postorder(int now)
{

    if (now == -1)
    {
       return;
    }
    

    postorder(tree[now].left);
    postorder(tree[now].right);
    cout << now << ' ';
    

}




int main()
{
    
    cin >> N;
    int x, y, z;
    for (int i = 0; i < N; i++)
    {
        cin >> x >> y >> z;
        tree[x].left = y;
        tree[x].right = z;
    }
    
    //1
    inorder(1);
    cout << '\n';
    //2
    preorder(1);
    cout << '\n';
    //3
    postorder(1);

}