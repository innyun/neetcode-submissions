class Solution {
public:
    int climbStairs(int n) {
        int a = 1;
        int b = 1;
        for (int i = 0; i < n - 1; i++) {
            int t = b;
            b = a + b;
            a = t;
        }
        return b;
    }
};
