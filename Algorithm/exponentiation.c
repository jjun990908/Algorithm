#include <stdio.h>

#define MAX_SIZE 1000
int power(int x, int n);

int main()
{
    int numTestCases;
    int answer;
    int x;
    int n;
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i){
        scanf("%d %d", &x, &n);
        answer = power(x,n);
        printf("%d",answer%1000);
        printf("\n");
    }
    return 0;
}

int power(int x, int n){
    int y;
    if (n == 0){
        return 1.0;
    }
    else if (n%2==1){
        y = power(x, (n-1)/2);
        if (y>1000){
            y = y%1000;
        }
        return x*y*y;
    }
    else{
        y = power(x,n/2);
        if (y>1000){
            y = y%1000;
        }
        return y*y;
    }
}