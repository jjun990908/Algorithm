#include <bits/stdc++.h>
#define FASTIO                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(0);
#define endl "\n"
using namespace std;

enum
{
    EMPTY = 0, WALL, GRAM
};

struct Point
{
    int y, x;
};

int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

int n, m, t;
vector<vector<int>> board;
Point gram;


int bfs(Point start, Point target)
{
    vector<vector<bool>> discovered(n, vector<bool>(m, false));
    queue<Point> q;

    discovered[start.y][start.x] = true;
    q.push(start);
    int cnt = 0;

    while (!q.empty())
    {
        int sz = q.size();
        while (sz--)
        {
            Point now = q.front();
            q.pop();

            if (now.y == target.y && now.x == target.x)
            {
                return cnt;
            }

            for (int i = 0; i < 4; i++)
            {
                Point next = {now.y + dy[i], now.x + dx[i]};

                if (next.y < 0 || next.y >= n || next.x < 0 || next.x >= m)
                    continue;
                if (discovered[next.y][next.x] == true)
                    continue;
                if (board[next.y][next.x] == WALL)
                    continue;
                
                q.push(next);
                discovered[next.y][next.x] = true;
            }
        }
        cnt++;
    }

    return 100001;
}


int main()
{
    FASTIO;

    cin >> n >> m >> t;
    board = vector<vector<int>>(n, vector<int>(m, 0));

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> board[i][j];
            if (board[i][j] == GRAM)
                gram = {i, j};
        }
    }
    int ans = std::min(bfs({0, 0}, {n-1, m-1}), bfs({0, 0}, {gram.y, gram.x}) + ((n-1) - gram.y + (m-1) - gram.x));

    if (ans <= t)
        cout << ans << endl;
    else
        cout << "Fail" << endl;

    return 0;
}