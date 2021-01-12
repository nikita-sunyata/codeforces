#include <iostream>

using namespace std;

int main(){
    int a,b;
    cin >> a >> b;
    int hour = a;
    //the rest is used candles
    int used = a;
    int add = 0;
    int rest = 0;
    while (used>=b){
        add = used/b;
        rest = used%b;
        hour += add;
        used = add+rest;
        //rest = 0; dont really need this since it will reset anyway
    }
    cout << hour << endl;
}
