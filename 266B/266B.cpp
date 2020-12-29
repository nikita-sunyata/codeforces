#include <iostream>
#include <string>
using namespace std;

int main(){
    int n,t;
    cin >> n >> t;
    string canteen_queue;
    cin >> canteen_queue;
    int current_index;
    current_index = 0;
    int people,time;
    people = n;
    time = t;
    char boy = 'B';
    char girl = 'G';
    for(int i=0;i<time;i++){
        for(current_index;current_index<people;current_index++){
            if(current_index==(people-1)){}else{
                if((canteen_queue[current_index]==boy)&&(canteen_queue[current_index+1]==girl)){
                    swap(canteen_queue[current_index+1],canteen_queue[current_index]);
                    //add additional one to skip the swapped people
                    current_index+=1;
                }
            }
        }
        //reset current_index
        current_index=0;
    }

    cout << canteen_queue << endl;
    //cout << canteen_queue[1] << endl;

}
