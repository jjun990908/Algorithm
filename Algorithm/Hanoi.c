#include <stdio.h>

#define MAX_SIZE 100
int answer = 0;
int history[MAX_SIZE];
void Hanoi(int n, int a, int b, int c);
int length(char n[]);
void swap(char *a, char *b);

int main()
{
    int numTestCases;
    int num;
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i){
        scanf("%d", &num);
        Hanoi(num, 1,2,3);
        printf("\n");
        answer = 0;
    }
    return 0;
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

void Hanoi(int n, int a, int b, int c){
    if (n>0){
        Hanoi(n-1, a,c,b);
        if (c==3){
            answer++;
            history[answer] = n;
            printf("%d ",n);
        }
        if (a==3){
            printf("%d ",history[answer-1]);
            answer--;
        }
        
        // printf("%d %d " ,a,c);
        Hanoi(n-1,b,a,c);
    }
}