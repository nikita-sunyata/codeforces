#include <iostream>
#include <string>
using namespace std;
int main(){
    string data;
    cin >> data;
    size_t found;
    found = data.find('h');
    if(found!=std::string::npos){
        found = data.find('e',found+1);
        if(found!=std::string::npos){
            found=data.find('l',found+1);
            if(found!=std::string::npos){
                found=data.find('l',found+1);
                if(found!=std::string::npos){
                    found=data.find('o',found+1);
                    if(found!=std::string::npos){
                        cout << "YES" << endl;
                    }else{cout << "NO" << endl;}
                }else{cout << "NO" << endl;}
            }else{cout << "NO" << endl;}
        }else{cout << "NO" << endl;}
    }else{cout << "NO" << endl;}
}
