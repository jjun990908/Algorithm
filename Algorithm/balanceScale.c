#include <stdio.h>

#define MAX_SIZE 1000
int balance(int a[], int n);
int KG[7] = {100,50,20,10,5,2,1};

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
        answer = balance(a,n);
        printf("%d\n",answer);
    }
    return 0;
}

int balance(int a[], int n){
    int sum_L=0;
    int sum_R=0;
    int answer=0;
    for (int i = 0; i<n; i++){
        if (sum_L<=sum_R){
            sum_L+= a[i];
        }
        else {
            sum_R+= a[i];
        }
    }
    int diff = 0;
    if(sum_L>=sum_R){
        diff = sum_L-sum_R;
    }
    else {
        diff = sum_R-sum_L;
    }

    if (diff ==0){
        return 0;
    }
    for (int i =0; i<7;i++){
        answer += diff/KG[i];
        diff %= KG[i];
    }
    return answer;
}