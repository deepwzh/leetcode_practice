class Solution {
public:
    string convert(string s, int numRows) {
        if (s.empty()) {
            return "";
        }
        if (numRows == 1) {
            return s;
        }
        string res;
        char chs[1000][1000];
        for (int i = 0; i < 1000; i++) {
            for (int j = 0; j < 1000; j++) {
                chs[i][j] = 0;
            } 
        }
        int cnt = 0;
        int block_size = ceil(1.0*s.size() / (numRows * 2 - 2));
        printf("%d\n", block_size);
        for (int i = 0; i < 2* block_size; i+=2) {
            for (int j = 0; j < numRows; j++) {
                chs[j][i] = (cnt < s.size() )?s[cnt++]: '\0';
            }
            for (int j = numRows - 2; j >= 1; j--) {
                chs[j][i+1] = (cnt < s.size() )?s[cnt++]: '\0';
            }
        }
        for (int j = 0; j < numRows; j++) {
            for (int i = 0; i < 2* block_size; i++) {
                // printf("%c", chs[j][i]?chs[j][i]:'#');
                if (chs[j][i]) res.push_back(chs[j][i]);
            }
            printf("\n");
        }
        return res;
    }
};