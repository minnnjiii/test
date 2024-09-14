#include <iostream>
#include <string>

using namespace std;

string str;
int a, b, c;


int main()
{
	cin >> str;

	cin >> a >> b >> c;

	for (int i = 0; i < c; i++)
	{
		string subs1 = str.substr(a,b-a+1);
		cout << subs1;
	}

}
