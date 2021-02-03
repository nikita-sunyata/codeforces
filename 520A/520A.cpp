#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;
int main(){
    int letters;
    cin >> letters;
    string data;
    cin >> data;
    unordered_map<char,int> my_dict;
    for(int i=0;i<letters;i++){
        my_dict[tolower(data[i])]++;
    }
    if(my_dict.size()==26){
        cout << "YES" << endl;
    }else{
        cout << "NO" << endl;
    }
}
