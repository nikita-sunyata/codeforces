#include <iostream>
#include <string>
using namespace std;

int main(){
    string one;
    string two;
    cin >> one >> two;
    int one_char;
    int two_char;
    int answer=0;
    for(int i=0;i<one.length();i++){
        one_char = int(tolower(one[i]));
        two_char = int(tolower(two[i]));
        if(one_char<two_char){
            answer -=1;
            break;
        }else if(one_char>two_char){
            answer +=1;
            break;
        }else{
            answer += 0;
        }
    }
    cout << answer << endl;
}
