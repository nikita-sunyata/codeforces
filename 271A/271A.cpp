#include <iostream>
#include <string>
#include <sstream>
#include <unordered_map>
using namespace std;

int main(){
    stringstream tmp;
    string string_data;
    int int_data;
    unordered_map<char,int> my_dict;
    cin >> string_data;
    tmp << string_data;
    tmp >> int_data;
    int_data+=1;
    tmp.clear();
    tmp << int_data;
    tmp >> string_data;
    //cout << string_data << "  S" << endl;
    //cout << int_data << "  I" << endl;
    int check = 0; //1=not pass,0=pass
    string answer;
    while(1){
        for(int i=0;i<string_data.length();i++){
            my_dict[string_data[i]]+=1;
            if (my_dict[string_data[i]]>1){
                check = 1;
                break;
            }
        }
        if(check!=1){
            answer  = string_data;
            break;
        }

        // year plus one
        tmp.clear();
        tmp << string_data;
        tmp >> int_data;
        int_data += 1;
        tmp.clear();
        tmp << int_data;
        tmp >> string_data;
        // clear dict
        my_dict.clear();
        // reset check to 0
        check = 0;

        
    }
    cout << answer << endl;
}
