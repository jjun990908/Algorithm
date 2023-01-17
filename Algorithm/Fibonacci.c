#include <stdio.h>

#define MAX_SIZE 1000
int Fibonacci(int n);

int main()
{
    int numTestCases;
    int answer;
    int a;
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i){
        scanf("%d", &a);
        answer = Fibonacci(a);
        printf("%d",answer);
        printf("\n");
    }
    return 0;
}

int Fibonacci(int n){
    int answer;
    if (n==0){
        return 0;
    }
    else if (n==1){
        return 1;
    }
    else{
        return Fibonacci(n-1) + Fibonacci(n-2);
    }
}