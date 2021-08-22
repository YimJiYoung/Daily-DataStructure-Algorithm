
// Design Linked List
// https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/



/**
 * Initialize your data structure here.
 */
 var MyLinkedList = function() {
    this.head = null;
};

/**
 * Get the value of the index-th node in the linked list. If the index is invalid, return -1. 
 * @param {number} index
 * @return {number}
 */
MyLinkedList.prototype.get = function(index) {
    let node = this.head;
    
    for (let i = 0; i <= index ; i++) {
        if (!node) {
            return -1;
        }
        if (i === index) {
            return node.val;
        }
        node = node.next;
    }
};

/**
 * Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtHead = function(val) {
    const newNode = { val: val, next: null }; 
    
    if (this.head) {
        newNode.next = this.head;
    }
    this.head = newNode;
};

/**
 * Append a node of value val to the last element of the linked list. 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtTail = function(val) {
    const newNode = { val: val, next: null };
    let node = this.head;
    
    while(node) {
        if (!node.next) {
            node.next = newNode;
            return;
        }
        node = node.next;
    }
    
    if (!node) {
        this.head = newNode;
    }
};

/**
 * Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. 
 * @param {number} index 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtIndex = function(index, val) {
    const newNode = { val: val, next: null };
    let prevNode = null;
    let node = this.head;
    
    if (!node || index == 0) {
      this.addAtHead(val);  
      return;
    }
    
    for (let i = 0; i <= index ; i++) {
        if (!node) {
            prevNode.next = newNode;
            return;
        }
        if (i === index) {
            newNode.next = node;
            prevNode.next = newNode;
            return;
        }
        prevNode= node;
        node = node.next;
    }
};

/**
 * Delete the index-th node in the linked list, if the index is valid. 
 * @param {number} index
 * @return {void}
 */
MyLinkedList.prototype.deleteAtIndex = function(index) {
    let prevNode = null;
    let node = this.head;
    
    for (let i = 0; i <= index ; i++) {
        if (!node) {
            return;
        }
        if (i === index) {
            if (prevNode === null) {
                this.head = node.next;
                return;
            }
            prevNode.next = node.next;
            return;
        }
        prevNode= node;
        node = node.next;
    }
};

/** 
 * Your MyLinkedList object will be instantiated and called as such:
 * var obj = new MyLinkedList()
 * var param_1 = obj.get(index)
 * obj.addAtHead(val)
 * obj.addAtTail(val)
 * obj.addAtIndex(index,val)
 * obj.deleteAtIndex(index)
 */