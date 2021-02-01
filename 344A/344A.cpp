#include <iostream>
#include <string>
using namespace std;
int main(){
    long test;
    long groups=1;
    cin >> test;
    string previous;
    // first data
    cin >> previous;
    string current;
    for(long i=0;i<(test-1);i++){
        cin >> current;
        if(previous!=current){
            groups+=1;
        }
        previous = current;
    }
    cout << groups << endl;
}
