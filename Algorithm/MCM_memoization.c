#include <stdio.h>
#define MAX_LENGTH 101
#define MIN(a,b) (((a)<(b))?(a):(b))

int dp[100][100];
int MatrixChain(int m[], int i, int j);

int main()
{
    int numTestCases;
    int matrix[MAX_LENGTH];
    int num,answer;
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i){
        scanf("%d", &num);
        for (int i=0;i<100;i++){
            for (int j = 0; j<=100; j++){
                dp[i][j] = -1;
            }
        }
        for (int j = 0; j < num+1; j++)
            scanf("%d", &matrix[j]);
        answer = MatrixChain(matrix,1,num);
        printf("%d\n",answer);
    }
    return 0;
}

int MatrixChain(int m[], int i, int j){
    if (i==j){
        return 0;
    }
    if (dp[i][j] != -1){
        return dp[i][j];
    }
    dp[i][j] = __INT_MAX__;
    for (int k=i;k<j;k++){
        dp[i][j] = MIN(dp[i][j], MatrixChain(m,i,k) + MatrixChain(m,k+1,j) + m[i-1] * m[k] * m[j]);
    }
    return dp[i][j];
}