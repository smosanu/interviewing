#include <iostream>

using namespace std;

int count_matching(int *a1, int lena1, int *a2, int lena2){
  int count = 0;

    cout << "a1.len: " << lena1 << endl;
    cout << "a2.len: " << lena2 << endl;

    int i1 = 0;
    int i2 = 0;
    while ((i1 < lena1) && (i2 < lena2))
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
  return count;
}

int main()
{
    // two arrays, sorted, distinct
    int a1[] = {0, 1, 5, 8, 23, 67, 89, 456, 890, 9004, 9999, };
    int a2[] = {1, 4, 8, 78, 89, 234, 459, 679, 2469, 9999, 101010};
    // int count = 0;

    int lena1 = sizeof(a1) / sizeof(int);
    int lena2 = sizeof(a2) / sizeof(int);

    cout << "Count = " << count_matching(a1, lena1, a2, lena2) << endl;
    
    return (0);
}