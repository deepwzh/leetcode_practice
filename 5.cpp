class Solution {
private:
public:
    Solution() {
        // max_len = 0;
    }
    int palindromic_length_even(string s, int pos) {
        int max_len = 0;
        for (int i = 0; pos - i >= 0 && pos + i+1 < s.size(); i++) {
            if (s[pos - i] == s[pos + i + 1]) {
                max_len = max(max_len, i * 2 + 2);
            } else {
                break;
            }
        }
        return max_len;
    } 
    int palindromic_length_odd(string s, int pos) {
        int max_len = 1;
        for (int i = 0; pos - i >= 0 && pos + i < s.size(); i++) {
            if (s[pos - i] == s[pos + i]) {
                max_len = max(max_len, i * 2 + 1);
            } else {
                break;
            }
        }
        return max_len;
    }
    string longestPalindrome(string s) {
        int max_len = 0;
        bool is_even = false;
        int pos = 0;
        for (int i = 0; i < s.size(); i++) {
            int len1 = palindromic_length_even(s, i);
            int len2 = palindromic_length_odd(s, i);
            if (len1 > max_len) {
                is_even = true;
                pos = i;
                max_len = len1;
            }
            printf("#%d\n", max_len);
            if (len2 > max_len) {
                is_even = false;
                pos = i;
                max_len = len2;
            }
            printf("#%d\n", max_len);
        }
        printf("%d\n", max_len);
        string res;
        if (is_even) {
            for (int i = pos - max_len/2 + 1; i <= pos + max_len/2; i++) {
                res.push_back(s[i]);
                // printf("%c", s[i]);
            }
        } else {
            for (int i = pos - max_len/2; i <= pos + max_len/2; i++) {
                res.push_back(s[i]);
                // printf("%c", s[i]);
            }
        }
        return res;
    }
};