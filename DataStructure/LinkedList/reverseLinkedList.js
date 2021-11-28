// Reverse Linked List
// https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1205/

var reverseList = function(head) {
    let prevNode = null;
    let nextNode = null;
    let node = head;
    
    while(node) {
        nextNode = node.next;
        node.next = prevNode;
        prevNode = node;
        node = nextNode;
    }
    
    return prevNode;
};