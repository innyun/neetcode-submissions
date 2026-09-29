class Solution {
public:
    bool isValid(string s) {
        std::unordered_map<char, char> mapping = {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };

        std::stack<char> st;

        for (char &c : s) {
            if (mapping.count(c)) {
                if (st.empty() || st.top() != mapping[c]) {
                    return false;
                }
                else {
                    st.pop();
                }
            }
            else {
                st.push(c);
            }
        }

        return st.empty();
    }
};
