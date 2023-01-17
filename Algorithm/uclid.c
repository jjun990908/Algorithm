#include <stdio.h>

#define MAX_SIZE 1000
int gcd(int a, int b);

int main()
{
    int numTestCases;
    int a,b,answer;
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i){
        scanf("%d %d", &a,&b);
        answer = gcd(a,b);
        printf("%d",answer);
        printf("\n");
    }
    return 0;
}

int gcd(int a, int b){
    if (b==0){
        return a;
    }
    else(
        return gcd(b,a%b);
    )
}

