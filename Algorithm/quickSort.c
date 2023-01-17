#include <stdio.h>

#define MAX_SIZE 1000
void quickSort_H(int v[], int low, int high);
void quickSort_L(int v[], int low, int high);
int partition_H(int a[], int low, int high);
int partition_L(int a[], int low, int high);
void setCount(int n);

int countCmpOps_L = 0;
int countSwaps_L = 0;
int countCmpOps_H = 0;
int countSwaps_H = 0;

int main()
{
    int numTestCases;

    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i)
    {
        int num;
        int a[MAX_SIZE],b[MAX_SIZE];

        scanf("%d", &num);
        for (int j = 0; j < num; j++)
            scanf("%d", &a[j]);
        countCmpOps_L = 0;
        countSwaps_L = 0;
        countCmpOps_H = 0;
        countSwaps_H = 0;
        for(int j=0;j<num;j++){
            b[j] = a[j];
        }
        quickSort_H(a,0,num-1);
        quickSort_L(b,0,num-1);
        printf("%d %d %d %d",countSwaps_H,countSwaps_L, countCmpOps_H,countCmpOps_L);
        printf("\n");
        }

    return 0; 
}

void swap(int* a, int* b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp; 
}

int partition_H(int a[], int low, int high){
    int i, j;
    int pivot;

    pivot = a[low];
    i = low - 1;
    j = high + 1;
    
    while(1){
        while(a[++i]<pivot){
            countCmpOps_H++;
        }
        countCmpOps_H++;
        while(a[--j]>pivot){
            countCmpOps_H++;
        }
        countCmpOps_H++;
        if (i<j){
            swap(&a[i],&a[j]);
            countSwaps_H++;
        }
        else{
            return j;
        }
    }
}

int partition_L(int a[], int low, int high){
    int i,j;
    int pivot, pivotpos,tmp;

    pivot = a[low];
    j = low;
    
    for(i=low+1; i<=high;i++){
        countCmpOps_L++;
        if(a[i]<pivot){
            j++;
            tmp = a[i];
            a[i] = a[j];
            a[j] = tmp;
            countSwaps_L++;
        }
    }
    pivotpos = j;
    tmp = a[low];
    a[low] = a[pivotpos];
    a[pivotpos] = tmp;
    countSwaps_L++;
    return pivotpos;
}

void quickSort_L(int v[], int low, int high)
{
    int pivotpos;

    if(high>low){
        pivotpos = partition_L(v,low,high);
        quickSort_L(v,low, pivotpos-1);
        quickSort_L(v,pivotpos+1,high);
    }
}

void quickSort_H(int v[], int low, int high)
{
    int pivotpos;

    if(high>low){
        pivotpos = partition_H(v,low,high);
        quickSort_H(v,low, pivotpos);
        quickSort_H(v,pivotpos+1,high);
    }
}