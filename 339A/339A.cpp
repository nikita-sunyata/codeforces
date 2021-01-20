#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(){
    string data;
    cin >> data;
    int ones = count(data.begin(),data.end(),'1');
    int twos = count(data.begin(),data.end(),'2');
    int threes = count(data.begin(),data.end(),'3');
    string answer;
    for(int i=0;i<ones;i++){
        answer += ("1+");
    }
    for(int i=0;i<twos;i++){
        answer += ("2+");
    }
    for(int i=0;i<threes;i++){
        answer += ("3+");
    }
    answer = answer.substr(0,answer.length()-1);
    cout << answer << endl;
}
