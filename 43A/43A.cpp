#include <iostream>
#include <unordered_map>

using namespace std;

int main(){

    unordered_map<string,long> my_dict;
    long test;
    cin >> test;
    string current_team;
    string answer;
    long current_max = -1;
    for(int i=0;i<test;i++){
        cin >> current_team;
        my_dict[current_team]+=1;
        if (my_dict[current_team]>current_max){
            current_max = my_dict[current_team];
            answer = current_team;
        }
    }
    cout << answer << endl;
}
