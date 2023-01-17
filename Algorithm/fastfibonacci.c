#include <stdio.h>

#define MAX_SIZE 1000
int fib(int n);
void multiply(int F[2][2], int M[2][2]);
void power(int F[2][2], int n);

int main()
{
    int numTestCases;
    int answer;
    int a;
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i){
        scanf("%d", &a);
        answer = fib(a);
        printf("%d",answer%1000);
        printf("\n");
    }
    return 0;
}
int fib(int n){
    int F[2][2] = {{1,1},{1,0}};
    if (n==0){
        return 0;
    }
    power(F, n-1);
    return F[0][0];
}

void power(int F[2][2], int n){
    if (n==0 || n == 1){
        return;
    }
    int M[2][2] = {{1,1},{1,0}};
    power(F,n/2);
    multiply(F,F);
    if (n%2 != 0){
        multiply(F,M);
    }
}
void multiply(int F[2][2], int M[2][2]){
    int x = F[0][0]*M[0][0] + F[0][1]*M[1][0];
    int y = F[0][0]*M[0][1] + F[0][1]*M[1][1];
    int z = F[1][0]*M[0][0] + F[1][1]*M[1][0];
    int w = F[1][0]*M[0][1] + F[1][1]*M[1][1];

    if (x>1000){
        x = x%1000;
    }
    if (y>1000){
        y = y%1000;
    }
    if (z>1000){
        z = z%1000;
    }
    if (w>1000){
        w = w%1000;
    }
    F[0][0] = x;
    F[0][1] = y;
    F[1][0] = z;
    F[1][1] = w;
}