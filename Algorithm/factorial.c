#include <stdio.h>

#define MAX_SIZE 1000
int Factorial(int n);

int main()
{
    int numTestCases;
    int answer;
    int a;
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i){
        scanf("%d", &a);
        answer = Factorial(a);
        printf("%d",answer%1000);
        printf("\n");
    }
    return 0;
}

int Factorial(int n){
    int answer;
    if (n==0){
        return 1;
    }
    else{
        answer = n*Factorial(n-1);
        if (answer%1000==0){
            return ((answer/1000)%100000);
        }
        else if (answer%100==0){
            return ((answer/100)%100000);
        }
        else if (answer%10==0){
            return ((answer/10)%100000);
        }
        else{
            return (answer%100000);
        }
    }
}