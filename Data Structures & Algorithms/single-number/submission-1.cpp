class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int i = 0;
        for (int &num : nums) {
            i = i ^ num;
        }
        return i;
    }
};
