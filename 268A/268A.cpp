#include <iostream>
#include <unordered_map>
using namespace std;

int main(){
    //map <color , how many host(1)/guest(2) have that color>
    unordered_map<int,int> map1;
    unordered_map<int,int> map2;
    int games;
    int host;
    int guest;
    long answer = 0;
    cin >> games;
    for(int i=0;i<games;i++){
        cin >> host;
        cin >> guest;
        map1[host]+=1;
        map2[guest]+=1;

    }
    for(auto i:map1){
        //check if guest have same color
        if(map2.find(i.first)==map2.end()){
            //do nothing
        }else{
            answer += (map1[i.first]*map2[i.first]);
        }
    }
    cout << answer << endl;
}

