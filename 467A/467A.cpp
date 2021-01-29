#include <iostream>
#include <sstream>

using namespace std;

int main(){
    //stringstream tmp;
    //string data;
    int number1;
    int number2;
    int test;
    int capacity;
    int answer = 0;
    cin >> test;
    for(int i=0;i<test;i++){
        /*
        tmp.clear();
        cin >> data;
        tmp << data[0];
        tmp >> number1;
        tmp.clear();
        tmp << data[2];
        tmp >> number2;
        //the start will clear tmp
        */
        cin >> number2 >> number1;
        capacity = number1 - number2;
        if(capacity>=2){
            answer += 1;
        }
    }
    cout << answer << endl;
}
