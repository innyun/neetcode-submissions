class Solution {
public:
    bool isPalindrome(string s) {
        int a = 0;
        int b = s.length() - 1;

        while (a < b) {
            if (!isalnum(s[a])) {
                a++;
            }
            else if (!isalnum(s[b])) {
                b--;
            }
            else if (tolower(s[a]) != tolower(s[b])) {
                return false;
            }
            else {
                a++;
                b--;
            }
        }

        return true;
    }
};
