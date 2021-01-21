#include <iostream>

using namespace std;

int main(){
    long data;
    cin >> data;

    int answer;
    int the_rest;

    answer = data/5;
    the_rest = data%5;
    if(the_rest==0){
        cout << answer << endl;
    }else{
        cout << answer+1 << endl; 
    }
    

}
