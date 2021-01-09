#include <iostream>
#include <unordered_map>
#include <array>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int strength , dragons;
    cin >> strength >> dragons;
    unordered_map<int,int> my_dict;
    // i should use vector instead of array
    // cuz i want the sort function
    int key_array[dragons];
    //vector<int> key_list;
    int dragon_str;
    int dragon_reword;
    for(int i=0;i<dragons;i++){
        cin >> dragon_str;
        cin >> dragon_reword;
        // now the same key is added together 
        my_dict[dragon_str] += dragon_reword;
        // so we will have to reduce the recounted key later 
        key_array[i] = dragon_str;
    }
    //now all the data is ready
    //sort the array first
    int check = 1;
    std::sort(key_array,key_array+dragons);
    //now we reduce the recounted key
    vector<int> key_list;
    int len_of_array = sizeof(key_array)/sizeof(key_array[0]);
    int last_element;
    for(int i=0;i<len_of_array;i++){
        if(i==0){
            key_list.push_back(key_array[i]);
            last_element = key_array[i];
        }else{
            if(key_array[i]==last_element){
            //do nothing
            }else{
                key_list.push_back(key_array[i]);
                last_element = key_array[i];
            }
        }
    }


    for(int i=0;i<key_list.size();i++){
        if(strength>key_list[i]){
            strength += my_dict[key_list[i]];
        }else{
            check = 0;
            break;
        }
    }
    if(check==0){
        cout << "NO" << endl;
    }else{
        cout << "YES"<< endl;
    }
}
