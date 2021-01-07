#include <iostream>
#include <vector>
#include <string>
#include <array>
using namespace std;

int main(){
    //create an answer string
    string answer;
    //take in the input string
    string data;
    cin >> data;
    //create a check list
    /*
    vector <char> check_list = {'a','e','i','o','u','y','A','E','I','O','U','Y'};
    */
    string check_string = "aeiouyAEIOUY";
    //check every index from data
    char check;
    for(int i=0;i<data.length();i++){
        check = data[i];
        if(check_string.find(check)!=std::string::npos){
            //do nothing
        }else{
            answer += '.';
            answer += tolower(check);
        }
    }
    cout << answer << endl;
}
