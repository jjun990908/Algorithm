#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

struct Point
{
    int y, x;
};

int dy[] = {-1, -1, -1, 0, 1, 1, 1, 0};
int dx[] = {-1, 0, 1, -1, -1, 0, 1, 1};

vector<vector<int>> board;
int ans = 0;
int n, m;

int bfs(int y, int x)
{
    vector<vector<bool>> discovered(n, vector<bool>(m, false));
    queue<Point> q;
    q.push({y, x});

    discovered[y][x] = true;
    int cnt = 0;

    while (!q.empty())
    {
        int sz = q.size();
        while (sz--)
        {
            Point now = q.front();
            q.pop();
            if (board[now.y][now.x] == 1)
            {
                return cnt;
            }

            for (int d = 0; d < 8; d++)
            {
                int ny = now.y + dy[d];
                int nx = now.x + dx[d];

                if (ny < 0 || ny >= n || nx < 0 || nx >= m)
                    continue;

                if (discovered[ny][nx])
                    continue;

                discovered[ny][nx] = true;
                q.push({ny, nx});
            }
        }
        cnt++;
    }

    return -1;
}

int main()
{
    cin >> n >> m;

    board = vector<vector<int>>(n, vector<int>(m, 0));

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> board[i][j];
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            ans = std::max(ans, bfs(i, j));
        }
    }

    cout << ans;
}