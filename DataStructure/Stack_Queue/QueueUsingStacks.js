/**
 * Initialize your data structure here.
 */
var MyQueue = function () {
  // 두 개의 stack 정의
  this.stack1 = []; // push할 때 사용
  this.stack2 = []; // pop할 때 사용
  this.length = 0;
};

/**
 * Push element x to the back of queue.
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function (x) {
  this.stack1.push(x);
  this.length++;
};

/**
 * Removes the element from in front of queue and returns that element.
 * @return {number}
 */
MyQueue.prototype.pop = function () {
  this.length--;
  if (this.stack2.length > 0) return this.stack2.pop();
  // stack2 비어 있으면 stack1의 요소 모두 stack2로 이동
  while (this.stack1.length > 0) this.stack2.push(this.stack1.pop());
  return this.stack2.pop();
};

/**
 * Get the front element.
 * @return {number}
 */
MyQueue.prototype.peek = function () {
  if (this.stack2.length > 0) return this.stack2[this.stack2.length - 1];
  while (this.stack1.length > 0) this.stack2.push(this.stack1.pop());
  return this.stack2[this.stack2.length - 1];
};

/**
 * Returns whether the queue is empty.
 * @return {boolean}
 */
MyQueue.prototype.empty = function () {
  return this.length === 0;
};
