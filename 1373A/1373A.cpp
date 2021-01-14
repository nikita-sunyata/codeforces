#include <iostream>

using namespace std;

int main(){
    long long test;
    cin >> test;
    for(long long i=0;i<test;i++){
        long long a,b,c;
        cin >> a >> b >> c;
        int answer1;
        int answer2;
        if(a<c){
            answer1 = 1;
        }else{
            answer1 = -1;
        }
        if(c<(a*b)){
            answer2 = b;
        }else{
            answer2 = -1;
        }
        cout << answer1 <<" "<< answer2 << endl;

    }
}
