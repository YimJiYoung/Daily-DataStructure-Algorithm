// Intersection of Two Linked Lists
// https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/

function getLength(head) {
    let node = head;
    let length = 0;
   while(node) {
       node = node.next;
       length++;
   } 
    return length;
}

var getIntersectionNode = function(headA, headB) {
    const lengthA = getLength(headA);
    const lengthB = getLength(headB);
    
    if (lengthA !== lengthB ) {
        for (let i = 0; i < Math.abs(lengthA - lengthB); i++) {
            if (lengthA > lengthB) {
                headA = headA.next;
            } else {
                headB = headB.next;
            }
        }
    }
    
    while(headA && headB) {
        if (headA === headB) {
            return headA;
        }
        headA = headA.next;
        headB = headB.next;
    }
    
    return null;
};

// 두 링크드 리스트의 마지막으로 align을 맞추는게 키 포인트! 

// var getIntersectionNode = function(headA, headB) {
//     let a = headA;
//     let b = headB;
    
//     while (a !== b) {
//         a = a === null ? headB : a.next;
//         b = b === null? headA : b.next;
//     }
    
//     return a;
// };