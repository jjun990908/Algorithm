#include <stdio.h>

#define MAX_SIZE 1000
void merge(int a[], int low, int mid, int high);
void mergeSort(int v[], int low, int high);
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
        mergeSort(a, 0, n-1);
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

void mergeSort(int v[], int low, int high){
    int mid;

    if(low== high){
        return;
    }
    mid = (low+high)/2;
    mergeSort(v, low, mid);
    mergeSort(v,mid+1, high);
    merge(v,low,mid,high);
}