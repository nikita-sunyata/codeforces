#include <iostream>
#include <unordered_map>
using namespace std;

int main(){
    string name;
    unordered_map<char,int> my_dict;
    cin >> name;
    for(int x;x<name.length();x++){
        my_dict[name[x]]++ ;
    }
    if((my_dict.size()%2) == 0){
        cout << "CHAT WITH HER!" << endl;
    }else{cout << "IGNORE HIM!" << endl;}
    return 0;
};
