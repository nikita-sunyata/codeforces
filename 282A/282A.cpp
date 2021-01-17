#include <iostream>
#include <string>
using namespace std;

int main(){
    long test;
    cin >> test;
    long value = 0;
    string data;
    for(long i=0;i<test;i++){
        cin >> data; 
        if(data.find('+')!=std::string::npos){
            value++;
        }else{
            value--;
        }
    }
    cout << value << endl;
}
