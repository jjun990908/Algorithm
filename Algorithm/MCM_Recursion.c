#include <stdio.h>
#define MAX_LENGTH 101

int MatrixChain(int m[], int i, int j);

int main()
{
    int numTestCases;
    int matrix[MAX_LENGTH];
    int num,answer;
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i){
        scanf("%d", &num);
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
    int k, count;
    int min = __INT_MAX__;

    for (k=i;k<j;k++){
        count = MatrixChain(m,i,k)+MatrixChain(m,k+1,j)+m[i-1]*m[k]*m[j];
        if (count < min){
            min = count;
        }
    }
    return min;
}