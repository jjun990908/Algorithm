#include <stdio.h>

#define MAX_SIZE 1000
int max(int a[], int n);

int main()
{
    int numTestCases;
    int n,answer;
    int a[MAX_SIZE];
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i){
        scanf("%d", &n);
        for (int j = 0; j < n; j++){
            scanf("%d", &a[j]);
        }
        answer = max(a,n);
        printf("%d",answer);
        printf("\n");
    }
    return 0;
}

int max(int a[], int n){
    if (n==1){
        return a[0];
    }
    int max_num = max(a,n-1);
    if (max_num> a[n-1]){
        return max_num;
    }
    else {
        return a[n-1];
    }
}