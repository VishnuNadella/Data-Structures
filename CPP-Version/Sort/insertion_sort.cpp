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

vector<int> insertion_sort(vector<int> arr)
{
    for (int i = 1; i < size(arr); i++)
    {
        int val = arr[i];
        int idx = i - 1;
        while (idx >= 0 && arr[idx] > val)
        {
            arr[idx + 1] = arr[idx];
            idx -= 1;
        }
        arr[idx + 1] = val;
    }
    return arr;
}

int main()
{
    vector<int> arr = arr_comprehension();
    vector<int> req_arr = insertion_sort(arr);
    cout << endl
         << "Sorted array is as follows:" << endl;
    for (int i : req_arr)
    {
        cout << i << "\t";
    }

    return 0;
}