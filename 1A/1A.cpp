#include <iostream>

using namespace std;

int main(){
    long long n , m , a;
    cin >> n >> m >> a;
    long long multi_w = n/a;
    long long multi_h = m/a;
    if(n%a != 0){
        multi_w += 1;
    }
    if(m%a != 0){
        multi_h += 1;
    }
    long long answer;
    answer = multi_w * multi_h;
    cout << answer << endl;
}
