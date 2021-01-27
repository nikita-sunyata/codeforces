#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

int main(){
    long n;
    string data;
    cin >> n >> data;
    unordered_map<char,long> my_dict;
    for(long i=0;i<n;i++){
        my_dict[data[i]]+=1;
    }
    if(my_dict['A']>my_dict['D']){
        cout << "Anton" <<endl;
    }else if(my_dict['A']<my_dict['D']){
        cout << "Danik" <<endl;
    }else{
        cout << "Friendship"<<endl;
    }

}
