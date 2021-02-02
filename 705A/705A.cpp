#include <iostream>
#include <string>
using namespace std;

int main(){
    int data;
    cin >> data;
    //init the starting sentence
    data = data-1;
    string answer = "I hate ";

    for(int i=0;i<data;i++){
        if (i%2==0){
            answer +=  "that I love ";
        }else{
            answer += "that I hate ";
        }
    }
    cout  << answer << "it" << endl;
}
