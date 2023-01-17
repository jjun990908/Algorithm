#include <stdio.h>
#define MAX_LENGTH 16

void printAnswer(int board[][MAX_LENGTH], int n);
int nQueen(int board[][MAX_LENGTH],int col, int n);
int isSafe(int board[][MAX_LENGTH], int row, int col, int n);

int main()
{
    int numTestCases;
    int answer,n;
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i){
        int board[MAX_LENGTH][MAX_LENGTH] ={0,};
        scanf("%d",&n);
        if(nQueen(board,0,n)==0){
            printAnswer(board, n);
        }
        printAnswer(board, n);
    }
    return 0;
}

int nQueen(int board[][MAX_LENGTH],int col, int n){
    if(col>=n){
        return 1;
    }
    for(int i=0; i<n; i++){
        if (isSafe(board,i,col,n)){
            board[i][col] = 1;
            if (nQueen(board,col+1,n)){
                return 1;
            }
            board[i][col] = 0;
        }
    }
    return 0;
}

int isSafe(int board[][MAX_LENGTH], int row, int col, int n){
    int i,j;
    for(i = 0; i < col; i++){
        if (board[row][i]){
            return 0;
        }
    }
    for(i = row,j = col;i >= 0 && j >= 0; i--, j--){
        if(board[i][j]){
            return 0;
        }
    }
    for(i = row,j = col; j >= 0 && i < n; i++, j--){
        if(board[i][j]){
            return 0;
        }
    }
    return 1;
}

void printAnswer(int board[][MAX_LENGTH], int n){
    int i,j;
    for(i = 0; i<n;i++){
        for(j = 0; j<n;j++){
            if (board[i][j]){
                printf("%d ",j+1);
            }
        }
    }
    printf("\n");
}