#include <iostream>
#include <string>
using namespace std;

int main(){
	string s;
	cin >>  s;
	int upper_count = 0;
	int lower_count = 0;
	string answer_upper;
	string answer_lower;
	for(int i=0;i<s.length();i++){
		if ( isupper(s[i]) ){
			upper_count += 1;
		}else{
			lower_count += 1;
		}
		answer_upper +=  toupper(s[i]);
		answer_lower += tolower(s[i]);
	}
	if(upper_count>lower_count){
		cout << answer_upper << endl;
	}else{
		cout << answer_lower << endl;
	}
	
}