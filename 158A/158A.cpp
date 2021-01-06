#include <iostream>
#include <array>

using namespace std;

int main(){
    int n,k;
    int answer=0;
    cin >> n >> k;
    int my_array[n];
    for(int i=0;i<n;i++){
        cin >> my_array[i];
    }
    for(int i=0;i<n;i++){
        if((my_array[i]>=my_array[k-1])&&(my_array[i]>0)){
            answer+=1;
        }
    }
    cout << answer << endl;
}
