/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func splitListToParts(root *ListNode, k int) []*ListNode {
    node := root
    cnt := 0
    for node != nil {
        node = node.Next
        cnt += 1
    }
    a, b := cnt / k, cnt%k
    res := make([]*ListNode, k)
    l_index := 0
    l_cnt := 0
    node = root
    new_head := &ListNode{0, nil}
    new_node := new_head
    for node != nil {
        ll := 0
        if (l_index +1) <= b {
            ll = a + 1
        } else {
            ll = a
        }
        fmt.Println(ll)
        if l_cnt == ll {
            res[l_index] = new_head.Next
            new_node = new_head 
            l_index++
            l_cnt = 0
        }
        new_node.Next = &ListNode{node.Val, nil}
        new_node = new_node.Next
        l_cnt += 1
        node = node.Next
    }
    res[l_index] = new_head.Next
    return res
}