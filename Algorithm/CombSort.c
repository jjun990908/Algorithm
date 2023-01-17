#include <stdio.h>

#define MAX_SIZE 1000
void combSort(int a[], int n);

int main()
{
    int numTestCases;

    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i)
    {
        int num;
        int a[MAX_SIZE];

        scanf("%d", &num);
        for (int j = 0; j < num; j++)
            scanf("%d", &a[j]);

        combSort(a, num);
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

/* comb sort 함수 */
void combSort(int a[], int n)
{
    int countCmpOps = 0; // 비교 연산자 실행 횟수 
    int countSwaps = 0; // swap 함수 실행 횟수

// comb sort 알고리즘 구현
    const double shrink = 1.3;
    int gap = n, swapped = 1;

    while(gap>1 || swapped){
        if ((gap/=shrink)<1){
            gap = 1;
        }
        swapped = 0;
        for(int j = 0; j < n-gap; j++){
            countCmpOps++;
            if (a[j]<= a[j+gap]){
                continue;
            }
            swapped = 1;
            swap(&a[j],&a[j+gap]);
            countSwaps++;
        }
    }

    printf("%d %d ", countCmpOps, countSwaps);
}