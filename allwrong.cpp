#include <iostream>
#include <string>
using namespace std;
// https://www.metacareers.com/profile/coding_puzzles/?puzzle=1082217288848574
string getWrongAnswers(int N, string C)
{
  string allwrong = C;
  for (int i = 0; i < N; i++)
  {
    allwrong[i] = (C[i] == 'A') ? 'B' : 'A';
  }
  return allwrong;
}

int main()
{
  string allright = "AAAAAAAAA";
  int len = allright.length();
  string allwrong = getWrongAnswers(len, "AAAAAAAAA");
  cout << "All right = " << allright << " and all wrong = " << allwrong << endl;
  return 0;
}