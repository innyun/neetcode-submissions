class Solution {
public:
    int search(vector<int>& nums, int target) {
        int a = 0;
        int b = nums.size();
        
        while (a <= b) {
            int m = (a + b) / 2;

            if (nums[m] == target) {
                return m;
            }
            else if (nums[m] > target) {
                b = m - 1;
            }
            else {
                a = m + 1;
            }
        }

        return -1;
    }
};
