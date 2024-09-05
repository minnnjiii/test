#include <iostream>
#include <string>
using namespace std;

string arr[3][3]
{
	{"BHC","BBQ","KFC"},
{"MC","7AVE","PAPA"},
"DHC","OBS","MOMS",
};

int dx[4] = { 0,-1,0,1 };
int dy[4] = { -1,0,1,0 };

int main()
{
	int y, x;
	cin >> y >> x;
	
	for (int i = 0; i < 4; i++)
	{
		if (y+dy[i] <3 && y + dy[i] >= 0 &&  x+dx[i] <3 && x + dx[i] >= 0)
		{
			cout << arr[y + dy[i]][x + dx[i]];

		}
	}
	
}
