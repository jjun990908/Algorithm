#include <stdio.h>
#define SIZE 4

void scanBoard(int board[SIZE][SIZE]);
void printBoard(int board[SIZE][SIZE]);
int checkN(int board[SIZE][SIZE], int row, int col, int n);
int solveSudoku(int board[SIZE][SIZE], int row, int col);

int main()
{
    int numTestCases;
    int answer;
    int board[SIZE][SIZE];
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i){
        scanBoard(board);
        if (solveSudoku(board,0,0) == 1){
            printBoard(board);
        }
    }
    return 0;
}

void scanBoard(int board[SIZE][SIZE]){
    int i,j;
    for (i = 0; i<SIZE;i++){
        for (j = 0; j<SIZE; j++){
            scanf("%d",&board[i][j]);
        }
    }
}

void printBoard(int board[SIZE][SIZE]){
    int i,j;
    for (i = 0; i<SIZE;i++){
        for (j = 0; j<SIZE; j++){
            printf("%d ",board[i][j]);
        }
        printf("\n");
    }
}

int checkN(int board[SIZE][SIZE], int row, int col, int n){
    int i,j;
    for( i = 0; i<=SIZE-1; i++){
        if (board[row][i] == n){
            return 0;
        }
    }

    for( i = 0; i<=SIZE-1; i++){
        if (board[i][col] == n){
            return 0;
        }
    }

    int startRow = row - row % 2;
    int startCol = col - col % 2;

    for (i = 0; i<2; i++){
        for (j = 0; j<2; j++){
            if (board[i+startRow][j+startCol]==n){
                return 0;
            }
        }
    }
    return 1;
}

int solveSudoku(int board[SIZE][SIZE], int row, int col){
    if (row == SIZE-1 && col == SIZE){
        return 1;
    }

    if (col == SIZE){
        row ++;
        col = 0;
    }

    if (board[row][col] >0){
        return solveSudoku(board,row,col+1);
    }
    for(int n = 1; n<=SIZE; n++ ){
        if (checkN(board,row,col,n)==1){
            board[row][col] = n;
            if(solveSudoku(board,row,col+1)==1){
                return 1;
            }
        }
        board[row][col] = 0;
    }
    return 0;
}
