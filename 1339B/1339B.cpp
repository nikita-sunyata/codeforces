#include <iostream>
#include <algorithm>
#include <array>
#include <string>
using namespace std;

int main(){
    long test;
    cin >> test;
    for(long t=0;t<test;t++){
        long data_number;
        cin >> data_number;
        long my_array[data_number];
        for(int i=0;i<data_number;i++){
            cin >> my_array[i];
        }
        sort(my_array,my_array+data_number);
        //create answer_array
        long answer_array[data_number];
        //start to arrange them with bigest smalles 2ndbigest.
        long start = 0;
        long end = data_number -1;
        long answer_index = data_number-1; // always subtract 2
        /*
        if data_number is an odd number , then won't trigger the last answer_array[answer_index-1]
        so there won't be an error.
        */
        while(start<=end){
            answer_array[answer_index] = my_array[end];
            if((answer_index-1)<0){}else{
            answer_array[answer_index-1] = my_array[start];
            }
            start ++;
            end--;
            answer_index -= 2;
        }
        //create answer string to store the answer
        string answer;
        for(long x=0;x<data_number;x++){
            answer += to_string( answer_array[x] ) + " ";
        }
        cout << answer << endl;
    }
}

