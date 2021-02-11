#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <stdlib.h>
using namespace std;

int main(){
    long long test;
    cin >> test;
    unordered_map<long long,long long> a_dict;
    unordered_map<long long,long long> b_dict;
    long long min_a;
    long long min_b;
    long long gifts;
    long long tmp1;
    long long tmp2;
    for(long long i=0;i<test;i++){
        cin >> gifts;
        //get a dict and min a
        for(long long j=0;j<gifts;j++){
            if(j==0){
                cin >> tmp1;
                a_dict[j]+=tmp1;
                min_a = tmp1;
            }else{
                cin >> tmp2;
                a_dict[j]+=tmp2;
                min_a = min(min_a,tmp2);
            }

        }
        //cout << "a min : " << min_a << endl;
        //get b dict and min b
        for(long long j=0;j<gifts;j++){
            if(j==0){
                cin >> tmp1;
                b_dict[j]+=tmp1;
                min_b = tmp1;
            }else{
                cin >> tmp2;
                b_dict[j]+=tmp2;
                min_b = min(min_b,tmp2);
            }

        }
        //cout << "b min : " << min_b << endl;
        //start computing answer
        long long a_rest;
        long long b_rest;
        long long same;
        long long answer = 0;
        for(long long k=0;k<gifts;k++){
            same = min(a_dict[k]-min_a,b_dict[k]-min_b);
        //    cout << "same : " << same << endl;
            a_rest = (a_dict[k]-min_a) - same;
        //    cout << "a_rest : " << a_rest << endl;
            b_rest = (b_dict[k]-min_b) - same;
         //   cout << "b_rest : " << b_rest << endl;
            answer += same;
            answer += a_rest;
            answer += b_rest;
          //  cout << "answer : " << answer << endl;
        }
        //remember to reset unordered_map at the end
        a_dict.clear();
        b_dict.clear();
        // print out the answer
        cout << answer << endl;
        // reset answer;
        answer = 0;
    }
}
