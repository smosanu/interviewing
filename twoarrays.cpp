#include <iostream>

using namespace std;

int main()
{
    // two arrays, sorted, distinct
    int a1[] = {0, 1, 5, 8, 23, 67, 89, 456, 890, 9004, 9999, };
    int a2[] = {1, 4, 8, 78, 89, 234, 459, 679, 2469, 9999, 101010};
    int count = 0;

    cout << "a1.size: " << sizeof(a1) / sizeof(int) << endl;
    cout << "a2.size: " << sizeof(a2) / sizeof(int) << endl;

    // for (int i1 = 0; i1 < sizeof(a1) / sizeof(int); i1++)
    int i1 = 0;
    int i2 = 0;
    while ((i1 < sizeof(a1) / sizeof(int)) & (i2 < sizeof(a2) / sizeof(int)))
    {
        cout << i1 << i2 << endl;
        if (a1[i1] == a2[i2])
        {
            count++;
            cout << "Matching: " << a1[i1] << " = " << a2[i2] << endl;
            i1++;
            i2++;
        }
        else if (a1[i1] < a2[i2]){
            i1++;
        }
        else {
            i2++;
        }
    }
    cout << "Count = " << count << endl;
    return (0);
}