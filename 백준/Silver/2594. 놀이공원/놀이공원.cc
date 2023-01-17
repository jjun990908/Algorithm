#include<iostream>
using namespace std;

int main() {
    int n, a[50], b[50];
    int startmin, tmp;
    int breaktime = 0;
    int start = 600, end = 600;
    
    cin >> n;
    
    for(int i=0; i<n; i++){
        cin >> a[i] >> b[i];
        a[i] = a[i]/100*60 + a[i] %100 -10;
        b[i] = b[i]/100*60 + b[i] %100 +10;
    }
    
    for(int i=0; i<n-1; i++){
        startmin = i;
        
        for(int j=i+1; j<n; j++){
            if (a[startmin] > a[j]) startmin = j;
        }
        
        tmp = a[i];
        a[i] = a[startmin];
        a[startmin] = tmp;
        
        tmp = b[i];
        b[i] = b[startmin];
        b[startmin] = tmp;
    }
    
    for(int i=0; i<n; i++){
        if(a[i] > end){
            if (a[i] -end > breaktime) breaktime = a[i] -end;
            if (b[i] > end) end = b[i];
            start = a[i];
        }
        else {
            if(b[i] > end) end = b[i];
        }
    }
    
    if(1320 - end > breaktime) breaktime = 1320 - end;
    
    cout << breaktime;
    return 0;
    
}