#include <iostream>
#include <string>

using namespace std;

int main(){
    string data;
    string data2;
    string reverse_data;
    cin >> data >> data2;
    for(int i=data.length()-1;i>=0;i--){
        reverse_data += data[i];
    }
    if (data2==reverse_data){
        cout << "YES" << endl;
    }else{
        cout << "NO" << endl;
    }
}
