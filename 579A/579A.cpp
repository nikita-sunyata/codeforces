#include <iostream>
#include <cmath>
#include <bitset>
#include <string>
using namespace std;

int main(){
    long data;
    cin >> data;
    string bit_data =  std::bitset<30>(data).to_string();

    /* belowing code is so wrong...
    long rest;
    rest = data - pow(2,int(log2(data)));
    int answer = 1+rest;
    cout << answer << endl;
    //cout << "data: " << data << endl;
    //cout << "log2(data): " << int(log2(data)) << endl;
    */
    int start = 0;
    int answer = 0;
    //cout << "string_bit_data : " << bit_data << endl;
    for(int i=0;i<bit_data.length();i++){
        if(bit_data[i]=='1'){
            answer++;
        }else{
            //do nothing
        }
        
        
        /*
        if(start==0){
            if(bit_data[i]=='1'){
                start = 1;
                answer+=1;
            }else{
                //do nothing
            }
        }else{
            answer++;
        }*/
    }
    cout << answer << endl;
}
