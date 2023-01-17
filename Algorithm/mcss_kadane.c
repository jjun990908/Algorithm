#include <stdio.h>

#define MAX_SIZE 1000
int mcss_k(int a[], int n, int *start, int *end);

int main()
{
    int numTestCases,start,end,answer;
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i)
    {
        int n;
        int a[MAX_SIZE];
        scanf("%d", &n);
        for (int j = 0; j < n; j++)
            scanf("%d", &a[j]);
        answer = mcss_k(a, n,&start,&end);
        printf("%d %d %d", answer,start ,end);
        printf("\n");
    }
    return 0; 
}

int mcss_k(int a[], int n, int *start, int *end){
    int i, j;
    int maxSum = 0, thisSum=0;
    *start = *end = -1;
    for(i = 0, j = 0; j<n; j++){
        thisSum += a[j];
        if (thisSum>maxSum){
            maxSum = thisSum;
            *start = i;
            *end = j;
        }
        else if (thisSum <=0){
            i = j+1;
            thisSum = 0;
        }
    }
    return maxSum;
}
