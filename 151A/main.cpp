#include <iostream>


using namespace std;

int main()
{

    int friends,bottles,milliliters,limes,slices,salt,mil_needs,salt_needs;
    cin >> friends >> bottles >> milliliters >> limes >> slices >> salt >> mil_needs >> salt_needs;
    int drinks_available , slice_available , salt_available;
    drinks_available = (bottles*milliliters)/(friends*mil_needs);
    slice_available = (limes*slices)/friends;
    salt_available = salt/(friends*salt_needs);
    int answer;
    answer = min<int>(drinks_available,slice_available);
    answer = min<int>(answer,salt_available);
    cout << answer;
    return 0;
}
