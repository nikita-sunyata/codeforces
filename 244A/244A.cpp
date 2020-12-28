#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

int main(){
    int n,k;
    cin >> n >> k;
    //the amount of children is k
    // ai is the segment each children chose to have
    // create a dict to store all ai value
    unordered_map<int,int> my_dict;
    for(int i=1;i<(k+1);i++){
        cin >> my_dict[i];
    }
    //just a value dictionary
    unordered_map<int,int> values;
    for(int i=1;i<(k+1);i++){
        values[my_dict[i]]+=1;
    }
    /*
    //test values
    cout << "your values dict is :" << endl;
    for (auto i : values) {
        cout << "{" << i.first << ": " << i.second << "}\n";
    }
    */

    int segments_amount_without_ai = n-1;
    //start printing every children's segments
    //create a value to store current number
    int current_number = 1;
    int part_two_needs = n-1;
    string second_part;

    //cout << "current_number = " << current_number << endl;
    //cout << "values[current_number] = " << values[current_number] << endl;

    for(int i=1;i<(k+1);i++){
        int first_part = my_dict[i];
        //calculate the second_part

        while(segments_amount_without_ai != 0){
                /*
                if(values.find(current_number)==values.end()){
                    //cout << (values.find(current_number) != values.end());
                    second_part += to_string(i);
                    second_part += " ";
                    current_number += 1;
                    segments_amount_without_ai -= 1;

                }else{
                    current_number += 1;
                }
                */
                if(values.find(current_number)!=values.end()){
                        current_number+=1;
                }else{
                    //cout << (values.find(current_number) != values.end());
                    //cout << "cannot find the key current number : " << current_number << endl;
                    //cout << "so the following string is going to add to second_part : " << i << endl;
                    second_part += to_string(current_number);
                    second_part += " ";
                    current_number += 1;
                    segments_amount_without_ai -= 1;
                }


        }
        //reset segments_amount_without_ai and second_part after print
        segments_amount_without_ai = n-1;
        cout << first_part << " " << second_part << endl;
        second_part = "";
        }


    /*
    for(auto i : my_dict){
        cout << i.first << " " << i.second << endl;
    }
    */
    return 0;
};
