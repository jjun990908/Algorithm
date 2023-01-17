#include <stdio.h>

#define MAX_SIZE 100
void Stringreverse(char n[],int i, int j);
void printstring(char n[],int size);
int length(char n[]);
void swap(char *a, char *b);

int main()
{
    int numTestCases;
    int len;
    char a[MAX_SIZE];
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i){
        scanf("%s", a);
        len = length(a);
        // printf("%d ",len);
        Stringreverse(a,0,len-1);
        // printf("%s",a);
        printstring(a,len);
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
void printstring(char n[], int size){
    for ( int i = 0; i<size; i++){
        printf("%c",n[i]);
    }
    printf("\n");
}
void swap(char *a, char *b)
{
    char tmp = *a;
    *a = *b;
    *b = tmp; 
}

void Stringreverse(char n[], int i, int j){
    char temp;
    if (i<j)
    {
        swap(&n[i],&n[j]);
        Stringreverse(n,i+1,j-1);
    }
    
}