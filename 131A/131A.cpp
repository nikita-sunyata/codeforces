#include <iostream>
#include <string>

using namespace std;

int main(){
    string data;
    cin >> data;
    string maybe_answer;
    int first_char;
    // if first char is upper then set to 1
    // else is set to 0
    for(int i=0;i<data.size();i++){
        if(i==0){
            if(isupper(data[i])){
                first_char = 1;
                maybe_answer += tolower(data[i]);
            }else{
                first_char = 0;
                maybe_answer += toupper(data[i]);
            }
        }else{
            if(first_char==1){
                if(isupper(data[i])){
                    maybe_answer += tolower(data[i]);
                }else{
                    break;
                }
            }else{
                if(isupper(data[i])){
                    maybe_answer += tolower(data[i]);
                }else{
                    break;
                }
            }
        }
    }
    if(data.size()==maybe_answer.size()){
        cout << maybe_answer << endl;
    }else{
        cout << data << endl;
    }
}
