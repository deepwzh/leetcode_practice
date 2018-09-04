/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
void solve(ListNode* & node, char * p) {
    // while(n) {
    if (*p == 0) return;
    // cout << n % 10 << endl;
    node = new ListNode(*p - '0');
    // if (is_first) {
    //     is_first = false;
    //     head = node;
    // }
    solve(node->next, p + 1);
    // }
}
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // long long n = 0;
        char s1[1000];
        char s2[1000];
        char s3[1000];
        int k1 = 0;
        while(l1) {
            s1[k1++] = l1->val + '0';
            l1 = l1->next;
            // k*=10;
        }
        int k2 = 0;
        while(l2) {
            s2[k2++] = l2->val + '0';
            // n += l2->val * k;
            l2 = l2->next;
            // k*=10;
        }
        int p1 = 0;
        int p2 = 0;
        int t = 0;
        int cnt = 0;
        while (p1 < k1 || p2 < k2 || t) {
            int d = t;
            if (p1 < k1) d += s1[p1++] - '0';
            if (p2 < k2) d += s2[p2++] - '0';
            s3[cnt++] = d % 10 + '0';
            t = d / 10;
        }
        s3[cnt] = 0;
        char * p = s3;
        ListNode * head = NULL;
        ListNode * node = NULL;
        bool is_first = true;
        solve(head, p);
        if (head == NULL) {
            head = new ListNode(0);
        }
        return head;
        
    }
};