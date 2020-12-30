#include <iostream>
#include <string>
using namespace std;

int main(){
    string data;
    cin >> data;
    bool check = false;
    for(int i=0;i<data.size();i++){
        char current_char = data[i];
        switch(current_char){
            case 'H':
                check = true;
                break;
            case 'Q':
                check = true;
                break;
            case '9':
                check = true;

        }
        if(check==true){
            break;
        }
    }
    if(check==true){
        cout << "YES" << endl;
    }else{
        cout << "NO" << endl;
    }
}
