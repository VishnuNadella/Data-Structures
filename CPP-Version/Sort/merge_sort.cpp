#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

vector<int> arr_comprehension()
{
    cout << "Input Array elements: ";
    vector<int> arr;
    string input;
    getline(cin, input);

    stringstream ss(input);
    int num;
    while (ss >> num)
    {
        arr.push_back(num);
    }

    return arr;
}

void merge_sort(vector<int> &arr) {
    if (size(arr) > 1) {
        int mid = size(arr) / 2;
        vector<int> L(arr.begin(), arr.begin() + mid);
        vector<int> R(arr.begin() + mid, arr.end());
        merge_sort(L);
        merge_sort(R);
        int i, j, k;
        i = 0;
        j = 0;
        k = 0;

        while (i < size(L) && j < size(R)) {
            if (L[i] < R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }
        while (i < size(L)) {
            arr[k] = L[i];
            i++;
            k++;
        }
        while (j < size(R)){
            arr[k] = R[j];
            j++;
            k++;
        }
    }
}

int main() {
    vector<int> arr = arr_comprehension();
    merge_sort(arr);
    for (int i: arr){
        cout << i << "\t";
    }
    return 0;
}