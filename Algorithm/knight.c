#include <stdio.h>

#define MAX_SIZE 9
#define MARK 1
#define UNMARK 0

typedef struct Point {int x,y;} point;
point direction[8] = {{1,-2},{2,-1},{2,1},{1,2},{-1,2},{-2,1},{-2,-1},{-1,-2}};
int board[MAX_SIZE][MAX_SIZE], path[MAX_SIZE][MAX_SIZE];
int knight(int m, int n , point pos, int counter);
void printpath(int m, int n);

int main()
{
    int numTestCases;
    int answer;
    int m, n, s, t;
    point start;
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i){
        scanf("%d %d %d %d", &m, &n, &s, &t);
        for (int j = 1; j<=m;j++){
            for (int k = 1; k<=n;k++){
                board[j][k] = UNMARK;
            }
        }
        start.x = s;
        start.y = t;
        board[start.x][start.y] = MARK;
        path[start.x][start.y] = 1;
        if (knight(m,n,start,1)){
            printf("1\n");
            printpath(m,n);
        }
        else {
            printf("0");
            printf("\n");
        }
    }
    return 0;
}

void printpath(int m, int n){
    for (int i =1; i<=m; i++){
        for (int j = 1; j<=n; j++){
            printf("%d ",path[i][j]);
            // printf("%d ",board[i][j]);
        }
        printf("\n");
    }
    return;
}

int knight(int m, int n, point pos, int counter){
    int i;
    point next;

    if (counter == n*m){
        return 1;
    }

    for (i = 0; i<8; i++){
        next.x = pos.x + direction[i].x;
        next.y = pos.y + direction[i].y;

        if (next.x>0 && next.y>0 && next.x<=m && next.y<=n && board[next.x][next.y] != MARK){
            board[next.x][next.y] = MARK;
            path[next.x][next.y] = counter+1;

            if (knight(m,n,next,counter+1)){
                return 1;
            }
            board[next.x][next.y] = UNMARK;
        }

    }
    return 0;
}