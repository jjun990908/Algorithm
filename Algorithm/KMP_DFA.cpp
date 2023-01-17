#include <iostream>
#define MAX_SIZE 1001

using namespace std;

void setDFA(int size);
void kmp(int n, int m);
int length(char n[]);
char a[MAX_SIZE], b[MAX_SIZE];
int answer;
int dfa[4][MAX_SIZE];

int main()
{
    int numTestCases; cin >> numTestCases;
    for(int i=0; i<numTestCases; i++)
    {
        for(int j=0; j<MAX_SIZE; j++){
            a[j] = ' ';
            b[j] = ' '; 
        }
        for(int j=0; j<4;j++){
            for(int k = 0; k<MAX_SIZE;k++){
                dfa[j][k] = 0;
            }
        }
        cin >> a >> b;
        int len_a = 0, len_b = 0, count = 0;
        answer = 0;
        len_a = length(a);
        len_b = length(b);
        setDFA(len_a);
        for(int j=0; j<4; j++){
            for(int k=0; k<=len_a; k++){
                if(dfa[j][k] != 0){
                    count++;
                }
            }
        }
        kmp(len_b,len_a);
        cout << count << " " << answer << endl;
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

void setDFA(int size){
    dfa[int(a[0])-65][0] = 1;
    int i=0;
    int j,k;
    for(j=1; j<size; j++){
        for(k=0; k<4; k++){
            dfa[k][j] = dfa[k][i];
        }
        if(size-1>=i){
            dfa[int(a[j])-65][j] = j+1;
        }
        i = dfa[int(a[j])-65][i];
    }
    for(k=0; k<4; k++){
        dfa[k][j] = dfa[k][i];
    }
}

void kmp(int n, int m){
    int i, j;
    for(i=0,j=0; i<n && j<=m; i++){
        j = dfa[int(b[i])-65][j];
        if(j==m){
            answer++;
        }
    }
}