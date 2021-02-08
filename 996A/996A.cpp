#include <iostream>

using namespace std;

int main(){
    long data;
    cin >> data;
    long rest;
    long answer;
    //start counting 100
    answer+= data/100;
    rest = data%100;
    // 20
    answer += rest/20;
    rest = rest%20;
    //10
    answer += rest/10;
    rest = rest%10;
    //5
    answer += rest/5;
    rest = rest%5;
    //1
    answer += rest/1;
    rest = rest%1;

    //answer
    cout << answer << endl;
    
}
