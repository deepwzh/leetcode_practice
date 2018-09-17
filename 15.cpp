class Solution {
private:
    struct Node {
        int a;
        int b;
        int c;
        Node (int a, int b, int c) {
            if (a > b) {
                swap(a, b);
            } 
            if (b > c) {
                swap(b, c);
            }
            if (a > b) {
                swap(a, b);
            }
            this->a = a;
            this->b = b;
            this->c = c;
        }
        bool friend operator < (const Node & node0, const Node & node) {
            if (node0.a == node.a) {
                if (node0.b == node.b) {
                    return (node0.c < node.c);
                } else {
                    return (node0.b < node.b);
                }
            } else {
                return (node0.a < node.a);
            }
        }
    };
public:
    int low_search(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (nums[mid] >= target) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
    int high_search(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (nums[mid] > target) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return high;
    }
    int search(vector<int>& nums, int target, int selected1, int selected2) {
        int low = low_search(nums, target);
        int high = high_search(nums, target);
        for (int i = low; i <= high; i++) {
            if (i != selected1 && i != selected2) {

                return i;
            }
        }
        return -1;
    }
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<Node> sets;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                int a = nums[i];
                int b = nums[j];
                int c = -(nums[i] + nums[j]);
                int pos = search(nums, c, i, j);
                if (pos != -1) {
                    sets.insert(Node(a, b, c));
                }
            }
        }
        vector<vector<int>>  res;
        for (set<Node>::iterator it = sets.begin(); it != sets.end(); it++) {
            vector<int> item;
            item.push_back((*it).a);
            item.push_back((*it).b);
            item.push_back((*it).c);
            res.push_back(item);
        }
        return res;
    }
};