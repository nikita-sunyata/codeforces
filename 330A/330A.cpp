#include <iostream>
#include <unordered_map>
using namespace std;

int main(){
	int r , c;
	cin >> r >> c;
	unordered_map<int,int>cant_eat_calumn;
	//start from 0 , add if there is toxic berry.
	int cant_eat_row = 0;
	// check is to check if there is toxic berry.
	char check;
	// if row_sub_check=1 , means that row can't eat.
	int row_sub_check = 0;
	//count the can't eat row 
	int row_sub = 0;
	for(int x=0;x<r;x++){
		for(int i=0;i<c;i++){
			cin >> check;
			if(check=='S'){
				if(row_sub_check==1){
					//already 1,so do nothing
				}else{
				row_sub_check = 1;
				}
				cant_eat_calumn[i]++;
			}else{
				//do nothing
			}
		}
		//count row_sub and reset row_sub_check
		if(row_sub_check==1){
			row_sub+=1;
			row_sub_check = 0;
		}
	}
	int can_eat_row = (r-row_sub);
	int can_eat_col = (c-cant_eat_calumn.size());
	int can_eat_row_cake = c*can_eat_row;
	int can_eat_col_cake = r*can_eat_col;
	int recounted = can_eat_row*can_eat_col;
	int answer = can_eat_row_cake + can_eat_col_cake - recounted;
	cout << answer << endl;
	//test
	/*
	cout << "can_eat_col : " << can_eat_col <<endl;
	cout << "can_eat_row : " << can_eat_row << endl;
	cout << "recounted : " << recounted << endl;
	cout << "can_eat_row_cake : " << can_eat_row_cake << endl;
	cout << "can_eat_col_cake : " << can_eat_col_cake << endl;
	*/
}	