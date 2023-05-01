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

int partition(int left, int right, vector<int> &arr) {
    int pivot_index = left;
    int p = arr[pivot_index];
    while (left < right) {
        while (left < arr.size() && arr[left] <= p){
            left++;
        }
        while (arr[right] > p) {
            right--;
        }
        if (left < right) {
            swap(arr[left], arr[right]);
        }
    }
    swap(arr[right], arr[pivot_index]);
    return right;    
}


/*
The reason why using d-- instead of d - 1 caused an infinite loop in Quick Sort is because the d-- expression decrements the value of d and then returns the new value.

In the quick_sort function, the d variable is the index of the pivot element after the partition function is called. This index is passed as the right parameter to the recursive quick_sort calls for the left and right subarrays.

If you use d-- instead of d - 1, the d variable will be decremented by 1, and then the new value will be passed as the right parameter to the recursive calls. This means that the same index will be used repeatedly, causing an infinite loop in some cases where the pivot element is not properly placed.

In contrast, using d - 1 correctly calculates the new right index and prevents an infinite loop in the Quick Sort algorithm.

*/


void quick_sort(int left, int right, vector<int> &arr) {
    if (left < right) {
        int d = partition(left, right, arr);
        quick_sort(left, d - 1, arr);
        quick_sort(d + 1, right, arr);
    }
}

int main() {
    vector<int> a = arr_comprehension();
    quick_sort(0, a.size() - 1, a);
    cout << "Sorted array is as follows: ";
    for (int i : a) {
        cout << i << "\t";
    }
    return 0;
}


