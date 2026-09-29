class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        std::unordered_map<char, int> m = {};

        for (int i = 0; i < s.length(); i++) {
            m[s[i]]++;
            m[t[i]]--;
        }

        for (auto& [key, value] : m) {
            if (value != 0) {
                return false;
            }
        }
        
        return true;
    }
};
