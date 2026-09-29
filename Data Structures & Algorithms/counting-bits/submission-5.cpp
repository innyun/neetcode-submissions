class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> out = {0};

        for (int i = 1; i <= n; i++) {
            out.push_back(out[i >> 1] + (i & 1));
        }

        return out;
    }
};
