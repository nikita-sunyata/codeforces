#include <iostream>

using namespace std;


int main(){
    long k , n , w;
    cin >> k >> n >> w;
    long requirement = 0;
    for(int i=1;i<=w;i++){
        requirement += i*k;
    }
    long need = requirement - n;
    if(need<0){
        need = 0;
    }
    cout << need << endl;
}
