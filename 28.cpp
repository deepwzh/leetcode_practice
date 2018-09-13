class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle == "")return 0;
        for (int i = 0; i < haystack.size(); i++) {
            bool find = true;
            for (int j = 0; j < needle.size(); j++) {
                if ((i + j) >= haystack.size() || (needle[j] != haystack[i+j])){
                    find = false;
                }
            }
            if (find) {
                return i;
            }
        }
        return -1;
    }
};