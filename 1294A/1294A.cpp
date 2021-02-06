#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    long long test;
    long a,b,c,n;
    cin >> test;
    long the_max;
    long need;
    long rest;
    for(long long i=0;i<test;i++){
        cin >> a >> b >> c >> n;
        if(max(a,b)==a){
            the_max = max(a,c);
        }else{
            the_max = max(b,c);
        }
        need = (the_max-a)+(the_max-b)+(the_max-c);
        if(need > n){
            cout << "NO" << endl;
        }else if(need == n){
            cout << "YES" << endl;
        }else{
            rest = n-need;
            if(rest%3==0){
                cout << "YES" << endl;
            }else{
                cout << "NO" << endl;
            }
        }
    }
}
