// Linked List Cycle
// https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/

// two pointer 전략
var hasCycle = function(head) {
    let firstPointer = head; // 2번 이동 
    let secondPointer = head; // 1번 이동
    
    while (firstPointer && secondPointer) {
        firstPointer = firstPointer.next;
        secondPointer = secondPointer.next; 
        
        if (!firstPointer) {
            return false;
        }
        
        firstPointer = firstPointer.next;
        
        if (firstPointer === secondPointer) { // 첫번째  포인터가 두번째 포인터 따라잡음 - 사이클 있음 ! 
            return true;
        }
    }
    
    return false;
};