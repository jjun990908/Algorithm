#include <stdio.h>

#define MAX_SIZE 100
int answer =0;
void Permutation(char n[],int begin, int end);
int length(char n[]);
void swap(char *a, char *b);
int get_ascii(char a);
int compute(char n[]);

int main()
{
    int numTestCases;
    char a[MAX_SIZE];
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i){
        answer = 0;
        scanf("%s", a);
        Permutation(a,0,length(a));
        printf("%d\n",answer);
    }
    return 0;
}
int get_ascii(char a){
    int n;
    char x = 'a';
    n = (int)x;
    int answer;
    answer = (int)a;
    return answer - n;
}
int length(char n[]){
    int len = 0;
    while(n[len]!='\0'){
        len++;
    }
    return len;
}
void swap(char *a, char *b)
{
    char tmp = *a;
    *a = *b;
    *b = tmp; 
}
int compute(char n[]){
    int sum =0;
    int len = length(n);
    for (int i = 0; i<len; i++){
        if (i%2==0){
            sum = sum + get_ascii(n[i]);
        }
        else {
            sum = sum - get_ascii(n[i]);
        }
    }
    // printf("%d\n",sum);
    return sum;
}

void Permutation(char *n, int begin, int end){
    int i;
    int range = end - begin;

    if (range==1){
        // printf("%s\n", n);
        if (compute(n)>0){
            answer++;
        }
    }
    else {
        for(i=0; i<range; i++){
            swap(&n[begin],&n[begin+i]);
            Permutation(n,begin+1,end);
            swap(&n[begin],&n[begin+i]);
        }
    }
}