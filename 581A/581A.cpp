#include <iostream>
#include <algorithm>
using namespace std;

int main(){
   long a;
   long b;
   long answer1;
   long answer2;
   cin >> a >> b;
   answer1 = min(a,b);
   answer2 = (max(a,b)-answer1)/2;
   cout << answer1 << " " << answer2 << endl;
}
