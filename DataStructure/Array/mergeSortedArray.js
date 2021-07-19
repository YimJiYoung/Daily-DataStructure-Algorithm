// Merge Sorted Array
// https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/

var merge = function(nums1, m, nums2, n) {
    let cursor1 = m - 1;
    let cursor2 = n - 1;
    let index = m + n - 1;
    
    while (cursor1 >= 0 && cursor2 >= 0) {
        if (nums1[cursor1] > nums2[cursor2]) {
            nums1[index--] = nums1[cursor1--];
        } else {
            nums1[index--] = nums2[cursor2--];
        }
    }
    
    while (cursor2 >= 0) {
       nums1[index--] = nums2[cursor2--];
    }
};