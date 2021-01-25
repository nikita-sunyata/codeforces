#include <iostream>
#include <string>
using namespace std;

int main(){
    long data,time;
    cin >> data >> time;
    for(long i=0;i<time;i++){
        if(data%10==0){
            data = data/10;
        }else{
            data = data-1;
        }
    }
    cout << data << endl;

}
