#include <iostream>
using namespace std;
#include <algorithm>
#include <limits.h>
#include <vector>

void rotateRight(int arr[], int n, int k) {
  k = k % n;

  reverse(arr, arr + n);
  reverse(arr, arr + k);
  reverse(arr + k, arr + n);
}

int main() {
  // int nums[3][4] = {{10, 20, 30, 40}, {50, 60, 70, 80}, {90, 100, 110, 120}};

  // for (int i = 0; i < 3; i++) {
  //   for (int j = 0; j < 4; j++) {
  //     cout << nums[i][j] << " ";
  //   }
  //   cout << endl;
  // }

  // cout << endl;
  // for (int j = 0; j < 4; j++) {
  //   for (int i = 0; i < 3; i++) {
  //     cout << nums[i][j] << " ";
  //   }
  //   cout << endl;
  // }

  /////////////////////////////////////////////////////////
  //// find max num in 2D array //////////////////
  /////////////////////////////////////////////////////////
  // int max_element = INT_MIN;

  // for (int j = 0; j < 4; j++) {
  //   for (int i = 0; i < 3; i++) {
  //     if (max_element < nums[i][j]) {
  //       max_element = nums[i][j];
  //     }
  //   }
  //   cout << endl;
  // }
  // cout << max_element;

  /////////////////////////////////////////////////////////
  //// Move negative numebrs to one side //////////////////
  /////////////////////////////////////////////////////////

  // int arr[] = {23, -7, 12, -10, -11, 50, 60};

  // int j = 0;

  // for (int i = 0; i < 7; i++) {
  //   if (arr[i] < 0) {
  //     swap(arr[i], arr[j]);
  //     j++;
  //   }
  // }

  /////////////////////////////////////////////////////////
  // shifting three numbers at a specific position  ///////
  /////////////////////////////////////////////////////////

  // for (int i = 0; i < 7; i++) {
  //   cout << arr[i] << " ";
  // }

  // int arr[] = {1, 0, 2, 2, 1, 0, 1, 0};

  // int left = 0;
  // int right = sizeof(arr) / sizeof(arr[0]) - 1;
  // int n = sizeof(arr) / sizeof(arr[0]);
  // int index = 0;

  // while (index <= right) {
  //   if (arr[index] == 0) {
  //     swap(arr[index], arr[left]);
  //     left++;
  //     index++;
  //   } else if (arr[index] == 2) {
  //     swap(arr[index], arr[right]);
  //     right--;
  //   } else {
  //     index++;
  //   }

  /////////////////////////////////////////////////////////
  ///  Move Zeros ///
  /////////////////////////////////////////////////////////

  // int nums[] = {0, 1, 0, 3, 12};

  // // int i = 0;
  // int n = sizeof(nums) / sizeof(nums[0]);
  // // int j = sizeof(nums) / sizeof(nums[0]);
  // int index = 0;

  // // for (int m = 0; m < n; m++) {
  // for (int m = 0; m < n; m++) {
  //   if (nums[m] != 0) {
  //     swap(nums[m], nums[index]);
  //     index++;
  //   }
  // }

  // for (int m = 0; m < n; m++) {
  //   cout << nums[m] << " ";
  // }

  /////////////////////////////////////////////////////////
  ////////////////  Rotate the array by k steps //////////
  /////////////////////////////////////////////////////////

  // int nums[] = {1, 2, 3, 4, 5};
  // int n = sizeof(nums) / sizeof(nums[0]);
  // int k = 2;

  // method 1:

  // rotateRight(nums, n, k);

  // for (int i = 0; i < n; i++) {
  //   std::cout << nums[i] << " ";
  // }

  // method 2:
  // vector<int> ans(n);

  // for (int i = 0; i < n; i++) {
  //   int newIndex = (i + k) % n;
  //   ans[newIndex] = nums[i];
  // }

  // for (int i = 0; i < n; i++) {
  //   std::cout << ans[i] << " ";
  // }

  /////////////////////////////////////////////////////////
  //////////////// row with maximum ones //////////
  /////////////////////////////////////////////////////////

  // https://leetcode.com/problems/row-with-maximum-ones/

  // class Solution {
  // public:
  //   vector<int> rowAndMaximumOnes(vector<vector<int>> &mat) {
  //     int row = mat.size();
  //     int max;
  //     int max_overall = 0;
  //     int index = 0;
  //     vector<int> ans;

  //     for (int i = 0; i < row; i++) {
  //       int col = mat[i].size();
  //       int max = 0;
  //       for (int j = 0; j < col; j++) {
  //         max = max + mat[i][j];
  //       }

  //       if (max > max_overall) {
  //         max_overall = max;
  //         index = i;
  //       }
  //     }
  //     ans.push_back(index);
  //     ans.push_back(max_overall);

  //     return ans;
  //   }
  // };

  /////////////////////////////////////////////////////////
  //////////////// 2 D rotation | rotate image   //////////
  /////////////////////////////////////////////////////////

  // class Solution {
  // public:
  //   void rotate(vector<vector<int>> &matrix) {
  //     int row = matrix.size();
  //     // int col = matrix[0].size();

  //     // transpose
  //     for (int i = 0; i < row; i++) {
  //       for (int j = i; j < matrix[i].size(); j++) {
  //         swap(matrix[i][j], matrix[j][i]);
  //       }
  //     }
  //     // reverse
  //     for (int i = 0; i < row; i++) {
  //       reverse(matrix[i].begin(), matrix[i].end());
  //     }
  //   }
  // };

  /////////////////////////////////////////////////////////
  //////////////// Two Sum                       //////////
  /////////////////////////////////////////////////////////

  // https://leetcode.com/problems/two-sum/description/

  // class Solution {
  // public:
  //   vector<int> twoSum(vector<int> &nums, int target) {
  //     int start = 0;
  //     int end = nums.size() - 1;
  //     int sum = 0;
  //     int n = nums.size();
  //     vector<int> ans;

  //     vector<pair<int, int>> indexedNums;
  //     for (int i = 0; i < n; i++) {
  //       indexedNums.push_back({nums[i], i});
  //     }

  //     sort(indexedNums.begin(), indexedNums.end());

  //     while (start < end) {
  //       sum = indexedNums[start].first + indexedNums[end].first;

  //       if (sum == target) {
  //         ans.push_back(indexedNums[start].second);
  //         ans.push_back(indexedNums[end].second);
  //         break;
  //       } else if (sum < target) {
  //         start++;
  //       } else {
  //         end--;
  //       }
  //     }
  //     return ans;
  //   }
  // };
}
