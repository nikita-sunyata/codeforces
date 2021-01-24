#include <iostream>

using namespace std;

int main(){
    long a , b;
    long year=0;
    cin >> a >> b;
    while(a<=b){
        a=a*3;
        b=b*2;
        year+=1;
    }
    cout << year << endl;
}
