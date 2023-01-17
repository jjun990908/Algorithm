#include <stdio.h>

#define MAX_SIZE 1000
void insertionSort(int a[], int n);

int main()
{
    int numTestCases;

    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i){
        int num;
        int a[MAX_SIZE];

        scanf("%d", &num);
        for (int j = 0; j < num; j++)
            scanf("%d", &a[j]);
        
        insertionSort(a, num);
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

/* Insertion Sort 함수 */
void insertionSort(int a[], int n)
{
    int countCmpOps = 0; // 비교 연산자 실행 횟수 
    int countSwaps = 0; // swap 함수 실행 횟수
    int tmp = 0,i,j;

    // insertion sort 알고리즘 구현
    // for (i = 1; i<n; i++){
    //     tmp = a[i];
    //     for(j = i-1; j>=0 && a[j] > tmp; j--){
    //         a[j+1] = a[j];
    //         countSwaps++;
    //     }
    //     a[j+1] = tmp;
    // }

    for (i = 1; i<n; i++){
        tmp = a[i];
        for (j = i-1; j>=0; j--){
            countCmpOps++;
            if (a[j] > tmp){
                a[j+1] = a[j];
                countSwaps++;
            }
            else{
                break;
            }
        }
        a[j+1] = tmp;
    }

    printf("%d %d ", countCmpOps, countSwaps);
}