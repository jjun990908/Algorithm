#include <stdio.h>

#define MAX_SIZE 1000
#ifndef max
#define max(a,b) (((a) > (b)) ? (a) : (b))
#endif

int mcss_dc(int a[], int start, int end);

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
        answer = mcss_dc(a,0,n-1);
        printf("%d", answer);
        printf("\n");
    }
    return 0; 
}

int mcss_dc(int a[],int start, int end){
    int i, j;
    if (start==end){
        return a[start];
    }
    int mid = (start + end)/2;
    int left =0;
    int right = 0;
    int sum = 0;

    for(i = mid; i>=start;i--){
        sum += a[i];
        left = max(left,sum);
    }
    sum = 0;
    for (i = mid+1;i<=end; i++){
        sum+= a[i];
        right = max(right,sum);
    }

    int single = max(mcss_dc(a,start,mid),mcss_dc(a,mid+1,end));
    return max(left + right,single);
}
