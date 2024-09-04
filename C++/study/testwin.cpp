#include <iostream>
#include <vector>

using namespace std;

// B17616번 등수 찾기
// 문제 접근 : 확실히 나보다 앞에 있는 사람들과 나보다 뒤에 있는 사람들의 수가 필요함


int N, M, X; // N명의 학생들, M번 질문, 등수를 알고 싶은 X학생
vector<int> upScore[100001];
vector<int> downScore[100001];
int upvisited[100001];
int downvisited[100001];


int U = 0, V = 0; // 가장 높은 등수, 가장 낮은 점수

void updfs(int num)
{
	for (int i = 0; i < upScore[num].size(); i++)
	{
		int next = upScore[num][i];
		if (upvisited[next] == 1)
		{
			continue;
		}
		U++;
		upvisited[next] = 1;
		updfs(next);
	}

}

void downdfs(int num)
{
	for (int i = 0; i < downScore[num].size(); i++)
	{
		int next = downScore[num][i];
		if (downvisited[next] == 1)
		{
			continue;
		}
		V++;
		downvisited[next] = 1;
		downdfs(next);
	}
}



int main() {

	cin >> N >> M >> X; // N명의 학생들, M번 질문, 등수를 알고 싶은 X학생 입력받기

	// 누가 더 잘했는지  M개  입력받기



	for (int i = 0; i < M; i++)
	{
		int A, B;
		cin >> A >> B; // A학생 점수 > B학생 점수

		downScore[A].push_back(B); // 나보다 점수가 낮은 애들
		upScore[B].push_back(A); // 나보다 점수가 높은 애들
	}
	
	updfs(X);
	downdfs(X);

	cout << U + 1 << ' ';
	cout << N - V;
	
	
	
}