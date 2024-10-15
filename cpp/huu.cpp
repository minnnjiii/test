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

string utf8_encode(const wstring& wstr);

string** map_data;  // 맵 정보. 예) map_data[0][1] - [0, 1]의 지형/지물
map<string, string*> allies;  // 아군 정보. 예) allies.at("A") - 플레이어 본인의 정보
map<string, string*> enemies;  // 적군 정보. 예) enemies.at("X") - 적 포탑의 정보
string* codes;  // 주어진 암호문. 예) codes[0] - 첫 번째 암호문

int map_height, map_width, num_of_allies, num_of_enemies, num_of_codes;

// 메모리 할당 해제
void free_memory() {
    for (int i = 0; i < map_height; ++i) {
        delete[] map_data[i];
    }
    delete[] map_data;
    for (auto& ally : allies) {
        delete[] ally.second;
    }
    for (auto& enemy : enemies) {
        delete[] enemy.second;
    }
    delete[] codes;
}

// 입력 데이터를 파싱하여 변수에 저장
void parse_data(string game_data) {
    // 입력 데이터를 문자열 스트림에 담기
    istringstream iss(game_data);
    string line;

    // 첫 번째 행 데이터 읽기
    getline(iss, line);
    istringstream header(line);
    header >> map_height >> map_width >> num_of_allies >> num_of_enemies >> num_of_codes;

    // 맵 정보를 읽어오기
    map_data = new string*[map_height];
    for (int i = 0; i < map_height; ++i) {
        map_data[i] = new string[map_width];
    }

    for (int i = 0; i < map_height; ++i) {
        getline(iss, line);
        istringstream row(line);
        for (int j = 0; j < map_width; ++j) {
            row >> map_data[i][j];
        }
    }

    // 기존의 아군 정보를 초기화하고 다시 읽어오기
    allies.clear();
    for (int i = 0; i < num_of_allies; ++i) {
        getline(iss, line);
        istringstream ally_stream(line);
        string ally_name;
        ally_stream >> ally_name;

        string* ally_data = new string[4];
        for (int j = 0; ally_stream >> ally_data[j]; ++j);

        allies[ally_name] = ally_data;
    }

    // 기존의 적군 정보를 초기화하고 다시 읽어오기
    enemies.clear();
    for (int i = 0; i < num_of_enemies; ++i) {
        getline(iss, line);
        istringstream enemy_stream(line);
        string enemy_name;
        enemy_stream >> enemy_name;

        string* enemy_data = new string[2];  // 예시로 2개의 데이터를 저장
        for (int j = 0; enemy_stream >> enemy_data[j]; ++j);

        enemies[enemy_name] = enemy_data;
    }

    // 암호문 정보를 읽어오기
    codes = new string[num_of_codes];
    for (int i = 0; i < num_of_codes; ++i) {
        getline(iss, codes[i]);
    }
}

// 내 탱크의 위치 찾기
int* find_my_position() {
    int* my_position = new int[2];
    my_position[0] = -1;
    my_position[1] = -1;
    for (int i = 0; i < map_height; ++i) {
        for (int j = 0; j < map_width; ++j) {
            if (map_data[i][j] == "A") {
                my_position[0] = i;
                my_position[1] = j;
                return my_position;
            }
        }
    }
    return my_position;
}

struct POS {
    int x;
    int y;
};

struct Tank_Data {
    int x;
    int y;
    int head;    //머리 방향
    int moves;    //현재 이동 횟수
    int b1;        //일반 포탄
    int b2;        //포탄
    bool fired = false;
    vector<string> path;    //현재 이동한 경로
};

//머리 돌리기

//길 찾기
void findGoal(POS start, POS end, vector<string>& result, int b2) {
    cout << "길찾기 시작\n";
    vector<vector<bool>> visited(map_height, vector<bool>(map_width, false));
    queue<Tank_Data> q;
    q.push({ start.x, start.y, 3, 0, 1, b2, false });
    visited[start.x][start.y] = true;

    int dx[4] = { -1, 1, 0, 0 };
    int dy[4] = { 0, 0, -1, 1 };

    while (!q.empty()) {
        Tank_Data current = q.front();
        q.pop();

        //포탑 상하좌우에 있는지 확인
        //왼쪽에 있을 때
        if (end.x > 0 && current.x == end.x - 1 && current.y == end.y) {
            //포탑 방향으로 탄 발사
            current.path.push_back("D F M");
            result = current.path;
            if (current.fired == true) {
                result[0] = ("T");
            }
            return;
        } 
        //오른쪽에 있을 때
        else if (end.x < map_width - 1 && current.x == end.x + 1 && current.y == end.y) {
            current.path.push_back("U F M");
            result = current.path;
            if (current.fired == true) {
                result[0] = ("T");
            }
            return;
        }
        //위에 있을 때
        else if (end.y > 0 && current.x == end.x && current.y == end.y - 1) {
            current.path.push_back("R F M");
            result = current.path;
            if (current.fired == true) {
                result[0] = ("T");
            }
            return;
        }
        //아래에 있을 때
        else if (end.y < map_height - 1 && current.x == end.x && current.y == end.y + 1) {
            current.path.push_back("L F M");
            result = current.path;
            if (current.fired == true) {
                result[0] = ("T");
            }
            return;
        }

        //상하좌우 이동
        for (int i = 0; i < 4; i++) {
            int nx = current.x + dx[i];
            int ny = current.y + dy[i];

            //범위 검사
            if (nx < 0 || ny < 0 || nx >= map_height || ny >= map_width) {
                continue;
            }

            //이미 간곳인지?
            if (visited[nx][ny]) {
                continue;
            }

            //포탄이 없을 땐 풀만 가능
            if (current.b2 == 0 && map_data[nx][ny] != "G") {
                continue;
            }

            //포탄이 있을 땐 나무/풀/탱크 가능
            if (current.b2 != 0 && (map_data[nx][ny] == "R" || map_data[nx][ny] == "W" || map_data[nx][ny] == "F")) {
                continue;
            }

            //ㄱㄱ
            visited[nx][ny] = true;

            //방향에 따른 명령어 입력
            string order = "";
            if (i == 0) {
                order = "U A";
            }
            else if (i == 1) {
                order = "D A";
            }
            else if (i == 2) {
                order = "L A";
            }
            else {
                order = "R A";
            }

            Tank_Data new_tank = current;
            new_tank.x = nx;
            new_tank.y = ny;
            new_tank.moves += 1;
            new_tank.path.push_back(order);

            //포탄 쓰기
            if (map_data[nx][ny] == "T" || map_data[nx][ny][0] == 'E') {
                new_tank.b2--;
                new_tank.fired == true;
            }
            q.push(new_tank);
        }
    }
    cout << "길 찾기 종료\n";
}

void findsup(POS start, POS end, vector<string>& result) {
    cout << "길찾기 시작\n";
    vector<vector<bool>> visited(map_height, vector<bool>(map_width, false));
    queue<Tank_Data> q;
    q.push({ start.x, start.y, 3, 0, 1, 0 });
    visited[start.x][start.y] = true;

    int dx[4] = { -1, 1, 0, 0 };
    int dy[4] = { 0, 0, -1, 1 };

    while (!q.empty()) {
        Tank_Data current = q.front();
        q.pop();

        //보급이 상하좌우에 있는지 확인
        //아래에 있을 때
        if (end.x > 0 && current.x == end.x - 1 && current.y == end.y) {
            //포탑 방향으로 탄 발사
            current.path.push_back("S");
            result = current.path;
            return;
        }
        //위에 있을 때
        else if (end.x < map_width - 1 && current.x == end.x + 1 && current.y == end.y) {
            current.path.push_back("S");
            result = current.path;
            return;
        }
        //오른쪽에 있을 때
        else if (end.y > 0 && current.x == end.x && current.y == end.y - 1) {
            current.path.push_back("S");
            result = current.path;
            return;
        }
        //왼쪽에 있을 때
        else if (end.y < map_height - 1 && current.x == end.x && current.y == end.y + 1) {
            current.path.push_back("S");
            result = current.path;
            return;
        }

        //상하좌우 이동
        for (int i = 0; i < 4; i++) {
            int nx = current.x + dx[i];
            int ny = current.y + dy[i];

            //범위 검사
            if (nx < 0 || ny < 0 || nx >= map_height || ny >= map_width) {
                continue;
            }

            //풀인가?
            if (map_data[nx][ny] != "G") {
                continue;
            }

            //이미 간곳인지?
            if (visited[nx][ny]) {
                continue;
            }

            //ㄱㄱ
            visited[nx][ny] = true;

            //방향에 따른 명령어 입력
            string order = "";
            if (i == 0) {
                order = "U A";
            }
            else if (i == 1) {
                order = "D A";
            }
            else if (i == 2) {
                order = "L A";
            }
            else {
                order = "R A";
            }

            Tank_Data new_tank = current;
            new_tank.x = nx;
            new_tank.y = ny;
            new_tank.moves += 1;
            new_tank.path.push_back(order);

            q.push(new_tank);
        }
    }
    cout << "길 찾기 종료\n";
}

int main() {
    wstring nickname = L"기본코드";
    string game_data = init(nickname);


    vector<string> result;
    POS start_point;
    POS end_point;
    POS sup_point = { -1, -1 };
    int order_idx = 0;
    int b2 = 0;
    int b1 = 0;
    bool end_sup = false;

    // while 반복문: 배틀싸피 메인 프로그램과 클라이언트(이 코드)가 데이터를 계속해서 주고받는 부분
    while (!game_data.empty()) {
        // 자기 차례가 되어 받은 게임정보를 파싱
        cout << "----입력데이터----\n" << game_data << "\n----------------\n";
        parse_data(game_data);

        // 파싱한 데이터를 화면에 출력하여 확인
        cout << "\n[맵 정보] (" << map_height << " x " << map_width << ")\n";
        for (int i = 0; i < map_height; ++i) {
            for (int j = 0; j < map_width; ++j) {
                cout << map_data[i][j] << " ";

                //포탑 위치
                if (map_data[i][j] == "X") {
                    end_point = { i, j };
                }

                //탱크 위치
                if (map_data[i][j] == "A") {
                    start_point = { i, j };
                }

                //보급 위치
                if (map_data[i][j] == "F") {
                    sup_point = { i, j };
                }
            }
            cout << endl;
        }

        cout << "\n[아군 정보] (아군 수: " << num_of_allies << ")\n";
        for (const auto& ally : allies) {
            string* value = ally.second;
            if (ally.first == "A") {
                cout << "A (내 탱크) - 체력: " << value[0] << ", 방향: " << value[1]
                    << ", 보유한 일반 포탄: " << value[2] << "개, 보유한 대전차 포탄: " << value[3] << "개\n";
                b2 = stoi(value[3]);
                b1 = stoi(value[2]);
            }
            else if (ally.first == "H") {
                cout << "H (아군 포탑) - 체력: " << value[0] << "\n";
            }
            else {
                cout << ally.first << " (아군 탱크) - 체력: " << value[0] << "\n";
            }
        }

        cout << "\n[적군 정보] (적군 수: " << num_of_enemies << ")\n";
        for (const auto& enemy : enemies) {
            string* value = enemy.second;
            if (enemy.first == "X") {
                cout << "X (적군 포탑) - 체력: " << value[0] << "\n";
            }
            else {
                cout << enemy.first << " (적군 탱크) - 체력: " << value[0] << "\n";
            }
        }

        cout << "\n[암호문 정보] (암호문 수: " << num_of_codes << ")\n";
        for (int i = 0; i < num_of_codes; ++i) {
            cout << codes[i] << endl;
        }

        //일단 탄 하나 먹어
        if (!end_sup && sup_point.x != -1 && b2 == 0 && order_idx == 0) {
            findsup(start_point, sup_point, result);
        }
        //길 찾기
        else {
            cout << "길 찾기 호출\n";
            findGoal(start_point, end_point, result, b2);

            cout << "결과\n";
            for (auto k : result) {
                cout << k << "\n";
            }
            cout << "\n";
        }    

        //근처 암호문이면 풀자
        if (num_of_codes > 0 && b2 == 0) {
            end_sup = true;
            string cipher = "JKLMNOPQRSTUVWXYZABCDEFGHI";

            for (int l = 0; l < 2; l++) {
                string output = codes[0];

                for (auto& c : output) {
                    c = cipher[(int)(c - 'A')];
                }
                string new_output = "G ";
                new_output += output;
                game_data = submit(new_output);
            }
        }

        if (result[0].find('M') != string::npos) {
            end_sup = false;
        }

        // 탱크의 동작을 결정하기 위한 알고리즘을 구현하고 원하는 커맨드를 output 변수에 담기
        // 코드 구현 예시 : '아래쪽으로 전진'하되, 아래쪽이 지나갈 수 있는 길이 아니라면 '오른쪽로 전진'하라
        
        string output = "S";  // 알고리즘 결괏값이 없을 경우를 대비하여 초기값을 S로 설정

            int* my_position = find_my_position();
            output = result[0];
            //내가 갈길이 탱크로 막히면 포탄 쏘자
            if (output[0] == 'U') {
                if (map_data[my_position[0] - 1][my_position[1]][0] == 'E') {
                    //포탄 발사
                    output = "U F S";
                    game_data = submit(output);
                }
            }
            else if (output[0] == 'D') {
                if (map_data[my_position[0] + 1][my_position[1]][0] == 'E') {
                    //포탄 발사
                    output = "D F S";
                    game_data = submit(output);
                }
            }
            else if (output[0] == 'L') {
                if (map_data[my_position[0]][my_position[1] - 1][0] == 'E') {
                    //포탄 발사
                    output = "L F S";
                    game_data = submit(output);
                }
            }
            else if (output[0] == 'R') {
                if (map_data[my_position[0]][my_position[1] + 1][0] == 'E') {
                    //포탄 발사
                    output = "R F S";
                    game_data = submit(output);
                }
            }

            if (output[0] == 'T') {
                if (map_data[my_position[0] - 1][my_position[1]][0] == 'T') {
                    //포탄 발사
                    result[0] = "U F S";
                }
                else if (map_data[my_position[0] + 1][my_position[1]][0] == 'T') {
                    //포탄 발사
                    result[0] = "D F S";
                }
                else if (map_data[my_position[0]][my_position[1] - 1][0] == 'T') {
                    //포탄 발사
                    result[0] = "L F S";
                }
                else if (map_data[my_position[0]][my_position[1] + 1][0] == 'T') {
                        //포탄 발사
                        result[0] = "R F S";
                }
            }

            delete[] my_position;

            output = result[0];

        //if (my_position[0] < map_height - 1 && map_data[my_position[0] + 1][my_position[1]] == "G") {
        //    output = "D A";
        //}
        //else {
        //    output = "R A";
        //}

        // while 문의 끝에는 다음 코드가 필수로 존재하여야 함
        // output에 담긴 값은 submit 함수를 통해 배틀싸피 메인 프로그램에 전달
        game_data = submit(output);
    }

    // 반복문을 빠져나왔을 때 배틀싸피 메인 프로그램과의 연결을 완전히 해제하기 위해 close 함수 호출
    free_memory();
    close();
    return 0;
}