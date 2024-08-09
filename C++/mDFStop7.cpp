#include <iostream>
#include <vector>

using namespace std;

// DFS_top_7_ 등수 찾기


struct student{

    int a;
    int b;

};

int N, M, X; // N명의 학생들, M번 질문, 등수를 알고 싶은 X학생
vector<student> graph; // A학생이랑 B학생이랑 누가 더 잘했는지 알려주는 그래프
int U, V; // 가장 높은 등수, 가장 낮은 점수



int main(){
    
    cin >> N >> M >> X; // N명의 학생들, M번 질문, 등수를 알고 싶은 X학생 입력받기
    
    // 누가 더 잘했는지  M개  입력받기
    for (int i = 0; i < M; i++)
    {
        int A, B;
        cin >> A >> B;
        graph.push_back({A,B});
    }
    


}