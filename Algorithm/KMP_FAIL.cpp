#include <iostream>
#define MAX_SIZE 1001

using namespace std;

void getFail(int size);
void kmp(int n, int m);
int length(char n[]);
char a[MAX_SIZE], b[MAX_SIZE];
int fail[MAX_SIZE], answer;

int main()
{
    int numTestCases; cin >> numTestCases;
    for(int i=0; i<numTestCases; i++)
    {
        for(int j=0; j<MAX_SIZE; j++){
            a[j] = ' ';
            b[j] = ' '; 
            fail[j] = 0;
        }
        cin >> a >> b;
        int len_a = 0, len_b = 0; answer = 0;
        len_a = length(a);
        len_b = length(b);
        getFail(len_a);
        kmp(len_b, len_a);
        for(int j=0; j<len_a; j++){
            cout << fail[j] << " ";
        }
        cout << endl;
        cout << answer << endl;
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

void getFail(int size){
    int i,j=0;
    for(i=1; i<size;i++){
        while(j>0 && a[i] != a[j]){
            j = fail[j-1];
        }
        if(a[i] == a[j]){
            fail[i] = ++j;
        }
    }
}

void kmp(int n, int m){
    int j =0;
    for(int i=0;i<n;i++){
        while(j>0 && b[i] != a[j]){
            j = fail[j-1];
        }
        if(b[i] == a[j]){
            if(j==m-1){
                answer++;
                j = fail[j];
            }
            else{
                j++;
            }
        }
    }
}