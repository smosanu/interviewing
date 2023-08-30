#include <iostream>
#include <vector>
using namespace std;

bool areTheyEqual(vector<int>& array_a, vector<int>& array_b){
  vector<int> la = array_a;
  vector<int> lb = array_b;
  sort(la.begin(), la.end());
  sort(lb.begin(), lb.end());
  for (int i=0; i<la.size(); i++){
    if (la[i] != lb[i]) return false;
  }
  return true;
}

int test_case_number = 1;

void check(bool expected, bool output) {
  bool result = (expected == output);
  const char* rightTick = "OK";//u8"\u2713";
  const char* wrongTick = "mM";//u8"\u2717";
  if (result) {
    cout << rightTick << "Test #" << test_case_number << "\n";
  }
  else {
    cout << wrongTick << "Test #" << test_case_number << ": Expected ";
    printf("%s", expected ? "true" : "false");
    cout << " Your output: ";
    printf("%s", output ? "true" : "false");
    cout << endl; 
  }
  test_case_number++;
}

int main(){
  vector <int> array_a_1{1, 2, 3, 4};
  vector <int> array_b_1{1, 4, 3, 2};
  bool expected_1 = true;
  bool output_1 = areTheyEqual(array_a_1, array_b_1); 
  check(expected_1, output_1); 

  vector <int> array_a_2{1, 2, 3, 4};
  vector <int> array_b_2{1, 4, 3, 3};
  bool expected_2 = false;
  bool output_2 = areTheyEqual(array_a_2, array_b_2); 
  check(expected_2, output_2); 
  
  return 0; 
}