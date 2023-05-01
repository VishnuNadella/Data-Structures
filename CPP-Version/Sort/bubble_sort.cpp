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

void swap(int *lf, int *rt)
{
    int temp = *rt;
    *rt = *lf;
    *lf = temp;
}

vector<int> bubble_sort(vector<int> arr)
{
    // not using for loop as we have to insert
    for (int i; i < size(arr); i++)
    {
        for (int j = i + 1; j < size(arr); j++)
        {

            if (arr[i] > arr[j])
            {
                int lf, rt;
                lf = arr[i];
                rt = arr[j];
                swap(&lf, &rt);
                arr[i] = lf;
                arr[j] = rt;
            }
        }
    }
    return arr;
}

int main()
{
    vector<int> arr = arr_comprehension();
    arr = bubble_sort(arr);
    cout << endl
         << "Sorted array as follows" << endl;
    for (int i : arr)
    {
        cout << i << "\t";
    }
}