#include <stdio.h>
#define MAX_LENGTH 101
#define MAX(a,b) ((a)>(b)?(a):(b))

int L[MAX_LENGTH][MAX_LENGTH], S[MAX_LENGTH][MAX_LENGTH];
int lengthLCS(char s[], char t[], int m, int n);
void printLCS(char s[], char t[], int m, int n);
int length(char n[]);

int main()
{
    int numTestCases;
    int m, n, answer;
    char a[MAX_LENGTH];
    char b[MAX_LENGTH];
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i){
        scanf("%s", a);
        scanf("%s", b);
        m = length(a);
        n = length(b);
        answer = lengthLCS(a,b,m,n);
        printf("%d\n",answer);
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

int lengthLCS(char s[], char t[], int m, int n){
    int a, b;
    if (m == 0 || n == 0) 
        return 0; 
    if (s[m-1] == t[n-1]) 
        return 1 + lengthLCS(s, t, m-1, n-1); 
    else
        a = lengthLCS(s, t, m, n-1);
        b = lengthLCS(s, t, m-1, n);
        return MAX(a,b);

}