#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int binary_search(vector<int> arr, int min_idx, int max_idx, int fnd){

    while (min_idx <= max_idx) {
        int mid = (min_idx + max_idx) / 2;
        if (arr[mid] == fnd) {
            return 1;
        } else if (arr[mid] > fnd) {
            max_idx = mid - 1;
        }else {
            min_idx = mid + 1;
        }
    }
    return 0;
}


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


int main() {
    cout << "Enter a sequence of numbers: ";
    vector<int> arr = arr_comprehension();
    int srch;
    cout << "Enter search number: ";
    cin >> srch;
    int resp = binary_search(arr, 0, size(arr), srch);
    if (resp) {
        cout << endl << "The number has been found" << endl;
    } else {
        cout << endl << "Number has not been found" << endl;
    }
}