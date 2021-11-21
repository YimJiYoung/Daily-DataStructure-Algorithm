//  Remove Linked List Elements
// https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1207/


/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
var removeElements = function(head, val) {
    const dummyNode = new ListNode(-1, head);
    let node = dummyNode;    
    
    while(node.next) {
        if(node.next.val === val) {
            node.next = node.next.next;
        }
        else {
            node = node.next;
        }
    }
    
    return dummyNode.next;
};