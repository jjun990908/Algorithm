#include <stdio.h>
#define MAX_LENGTH 101
#define MIN(a,b) ((a)>(b)?(b):(a))

int m[MAX_LENGTH][MAX_LENGTH];
int store[MAX_LENGTH][MAX_LENGTH];
int MatrixChain(int m[], int n);
void order (int i, int j);

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
        answer = MatrixChain(matrix,num+1);
        order(1,num);
        printf("\n%d\n",answer);
    }
    return 0;
}

int MatrixChain(int p[], int n){
    int i,j,k,L,q;
    for (i = 1; i<n; i++){
        m[i][i] = 0;
    }
    for(L=2;L<n;L++){
        for(i=1;i<n-L+1;i++){
            j = i+L-1;
            m[i][j] = __INT_MAX__;
            for (k=i;k<=j-1;k++){
                q = m[i][k]+ m[k+1][j]+p[i-1]*p[k]*p[j];
                if (q<m[i][j]){
                    m[i][j] = q;
                    store[i][j] = k;
                }
            }
        }
    }
    return m[1][n-1];
}

void order(int i, int j){
    if (i==j){
        printf("M%d",i);
    }
    else{
        int k = store[i][j];
        printf("(");
        order(i,k);
        order(k+1,j);
        printf(")");
    }
}