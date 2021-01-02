#include <iostream>
//using namespace std;

int main(){
    int lowest; // since the max won't be more than 10000
    int highest; // since the min should be at least 1
    int amazing_count = 0;
    int data_quantity;
    int check;
    std::cin >> data_quantity;
    for(int i=0;i<data_quantity;i++){
        std::cin >> check;
        if(i==0){
            lowest = check;
            highest = check;
        }else{
            if(check>highest){
                highest = check;
                amazing_count++;
            }else if(check<lowest){
                lowest = check;
                amazing_count++;
            }else{
                //do nothing
            }
        }
    }
    std::cout << amazing_count;
}
