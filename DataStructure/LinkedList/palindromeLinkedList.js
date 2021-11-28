//  Palindrome Linked List
// https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1209/

// 재귀 이용
//  var frontNode = null;
//  var checkPalindrome = function(currentNode) {
//      if(currentNode) {
//          if (!checkPalindrome(currentNode.next)) {
//              return false;
//          }
//          if (currentNode.val !== frontNode.val) {
//              return false;
//          }
//          frontNode = frontNode.next;
//      }
//      return true;
//  }
 
//  var isPalindrome = function(head) {
//     frontNode = head;
//     return checkPalindrome(head);
//  };


var isPalindrome = function(head) {
    if (!head) {
        return true;
    }
    
    // 1. Find the end of the first half.
    const haflNode = getNodeInMiddle(head);
    
   // 2. Reverse the second half.
    const secondHalfHead = reverseLikedList(haflNode);
    
    // 3. Determine whether or not there is a palindrome.
    let firstNode = head;
    let secondNode = secondHalfHead;
    
    while (firstNode && secondNode) {
        if (firstNode.val !== secondNode.val) {
            return false;
        }
        firstNode = firstNode.next;
        secondNode = secondNode.next;
    }
    
    return true;
};

var reverseLikedList = function(head) {
    let prevNode = null;
    let node = head;
    
    while(node) {
        const nextNode = node.next;
        node.next = prevNode;
        prevNode = node;
        node = nextNode;
    }
    
    return prevNode;
}

var getNodeInMiddle = function(head) {
    let length = 1;
    let node = head;
    
    // get linked list's length
    while(node.next) {
        length++;
        node = node.next;
    }
    
    // get the node in the middle
    node = head;
    for(let index = 0; index < Math.floor(length / 2); index++) {
         node = node.next;
    }
    
    return node;
}