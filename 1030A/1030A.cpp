#include <iostream>
using namespace std;

int main(){
    int test;
    int data;
    int answer = 0;
    cin >> test;
    for(int i=0;i<test;i++){
        cin >> data;
        if(data==1){
            answer = 1;
        }
    }
    if(answer==0){
        cout << "EASY" << endl;
    }else{
        cout << "HARD" << endl;
    }
}
