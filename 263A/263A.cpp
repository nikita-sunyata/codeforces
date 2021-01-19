#include <iostream>
#include <cmath>

using namespace std;

int main(){
    int row;
    int col;
    int current_number;
    int row_move;
    int col_move;
    for(int i=0;i<25;i++ ){
        cin >> current_number;
        row = (i/5)+1;
        col = (i%5)+1;
        //cout << "(" << row << "," << col << ")" << endl;
        if(current_number==1){
            row_move=abs(row-3);
            col_move=abs(col-3);
            //break; can't break because there is still test data to be input.
        }
    }
    cout << row_move + col_move << endl;
}
