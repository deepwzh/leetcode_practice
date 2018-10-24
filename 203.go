/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func removeElements(head *ListNode, val int) *ListNode {
    var new_head *ListNode = &ListNode{Val: 0, Next: nil}
    new_head.Next = head
    node := new_head
    for node != nil {
        for node.Next != nil && node.Next.Val == val {
            node.Next = node.Next.Next
        }
        node = node.Next
    }
    node = nil
    return new_head.Next
}
