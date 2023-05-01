#include <iostream>
#include <sstream>
#include <vector>

using namespace std;
vector<int> arr_comprehension() {
    vector<int> arr; 
    string input;
    getline(cin, input); 

    stringstream ss(input);
    int num;
    while (ss >> num) { 
        arr.push_back(num);
    }

    return arr;
}


int linear_search(vector<int> arr, int fnd){
    for (int x: arr) {
        if (x == fnd){
            return 1;
        }
    }
    return 0;

}


int main() {
    cout << "Enter array elements: ";
    vector<int> arr = arr_comprehension();
    cout << "Enter a number to search for: ";
    int srch;
    cin >> srch;

    int resp = linear_search(arr, srch);
    if (resp) {
        cout << endl << "Element exists";
    } else {
        cout << endl << "Element does not exists";
    }
    return 0;
}