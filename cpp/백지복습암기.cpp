#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <string>
#include <locale>
#include <codecvt>
#include "libs/bridge.h"

#include <queue>

using namespace std;

struct POS {
    int x;
    int y;
};


struct Tank_Data {
    int x;
    int y;
    int head;
    int moves;
    int b1;
    int b2;
    bool fired = false;
    vector<string> path; 
};




void findGoal(POS start, POS end, vector<string>& result, int b2)
{

    cout << "길찾기 시작\n";
    vector<vector<bool>> visited(map_height, vector<bool>(map_width, false));
    queue<Tank_Data> q;
    q.push({start.x, start.y, 3, 0, 1, b2, false});
    visited[start.x][start,]
}