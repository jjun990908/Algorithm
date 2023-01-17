#include <stdio.h>
#ifndef MIN
#define MIN(a,b) (((a) > (b)) ? (b) : (a))
#endif

#define MAX_SIZE 1000
void merge(int a[], int low, int mid, int high);
void mergeSortIter(int v[], int n);
int countCmpOps;

int main()
{
    int numTestCases;
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i)
    {
        int n;
        int a[MAX_SIZE];
        countCmpOps = 0;
        scanf("%d", &n);
        for (int j = 0; j < n; j++)
            scanf("%d", &a[j]);
        mergeSortIter(a,n);
        printf("%d", countCmpOps);
        printf("\n");
    }
    return 0; 
}

void merge(int a[], int low, int mid, int high)
{
    int i,j,k;
    int tmp[MAX_SIZE];

    for(i=low; i<=high; i++){
        tmp[i] = a[i];
    }
    i = k = low;
    j = mid + 1;
    while (i<=mid && j<=high){
        if (tmp[i] <= tmp[j]){
            a[k++] = tmp[i++];
        }
        else{
            a[k++] = tmp[j++];
        }
        countCmpOps++;
    }
    while (i<=mid){
        a[k++] = tmp[i++];
    }
    while (j<=high){
        a[k++] = tmp[j++];
    }
}

void mergeSortIter(int v[], int n){
    int size = 1;
    while (size<n){
        for(int i = 0; i<n; i+=(2*size)){
            int low = i;
            int mid = low+size -1;
            int high = MIN(i+2*size-1,n-1);
            if(mid >= n-1){
                break;
            }
            merge(v, low, mid, high);
        }
        size *= 2;
    }
}