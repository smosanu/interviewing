#include <iostream>
#include <vector>
using namespace std;

int main()
{
    // arrays and vectors are natively supported in C++
    int my_array[5] = {10, 20, 30, 40, 50};
    int autosized_array[] = {12, 23, 34};
    char autochar[] = "ha ha, hello world like this!";
    cout << "my_array values: " << my_array[0] << ", " << my_array[1] << ", " << my_array[2] << ", " << my_array[3] << ", " << my_array[4] << endl;
    cout << "autosized_array values: " << autosized_array[0] << ", " << autosized_array[1] << ", " << autosized_array[2] << endl;
    cout << autochar << endl;

    int my_2d_array[4][5];
    my_2d_array[2][3] = 2345;
    cout << "my 2d array value at (2,3) = " << my_2d_array[2][3] << endl;
    cout << "my 2d array value at (0,1) = " << my_2d_array[0][1] << " (was not initialized)" << endl;

    vector<int> even_digits;
    even_digits.push_back(0);
    even_digits.push_back(2);
    even_digits.push_back(4);
    even_digits.push_back(6);
    even_digits.push_back(8);
    cout << "even digits: " << even_digits[0] << even_digits[1] << even_digits[2] << even_digits[3] << even_digits[4] << endl;
    cout << "even digits size: " << even_digits.size() << endl;

    return (0);
}