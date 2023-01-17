#include <stdio.h>
#define MAX_SIZE 1000

int count = 0;
void swap(int* a, int* b);
void fixHeap(int a[], int N, int i);
void heapSort(int a[], int N);

int main()
{
    int numTestCases;
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i)
    {
        count = 0;
        int N;
        int a[MAX_SIZE];
        scanf("%d", &N);
        for (int j = 0; j < N; j++){
            scanf("%d", &a[j]);
        }
        heapSort(a,N);
        printf("%d\n",count);
    }
    return 0; 
}

void heapSort(int a[], int N)
{

	for (int i = N / 2 - 1; i >= 0; i--)
		fixHeap(a, N, i);
	for (int i = N - 1; i >= 0; i--) {
		swap(&a[0], &a[i]);
		fixHeap(a, i, 0);
	}
}
void fixHeap(int a[], int N, int i)
{
	int max = i;
	int left = 2 * i + 1;
	int right = 2 * i + 2;
	if (left < N && a[left] > a[max])
		max = left;
	if (right < N && a[right] > a[max])
		max = right;
    if (right < N){
        count++;
    }
    if (left < N){
        count++;
    }
	if (max != i) {
		swap(&a[i], &a[max]);
		fixHeap(a, N, max);
	}
}
void swap(int* a, int* b)
{
	int temp = *a;
	*a = *b;
	*b = temp;
}