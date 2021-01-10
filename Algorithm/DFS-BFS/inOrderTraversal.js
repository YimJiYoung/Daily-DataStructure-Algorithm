// Binary Tree Inorder Traversal
// https://leetcode.com/problems/binary-tree-inorder-traversal/

// recursion
var inorderTraversal = function (root) {
  const order = [];
  traversal(root, order);
  return order;
};

function traversal(node, order) {
  if (!node) return order;

  traversal(node.left, order);
  order.push(node.val);
  traversal(node.right, order);
}

// using while
var inorderTraversal = function (root) {
  const stack = [];
  const order = [];
  let curNode = root;

  while (curNode !== null || stack.length > 0) {
    while (curNode !== null) {
      // 왼쪽 노드로 이동하면서 스택에 추가
      stack.push(curNode);
      curNode = curNode.left;
    }
    curNode = stack.pop();
    order.push(curNode.val);
    curNode = curNode.right;
  }
  return order;
};
