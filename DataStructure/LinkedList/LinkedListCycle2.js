// Linked List Cycle II
// https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/

// two pointer + floyd cycle 
 var detectCycle = function(head) {
    let p = head;
    let q = head;
    
    let intersection = null;
    
    while (p && q && p.next) {
        p = p.next.next;
        q = q.next; 
        
        if (p === q) {
            intersection = p;
            break;
        }
    }
    
    if (!intersection) {
        return null;
    }
    
    p = head;
    q = intersection;
    
    while(p !== q) {
        p = p.next;
        q = q.next;
    }
    
    return p;
};
