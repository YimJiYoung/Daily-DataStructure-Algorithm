// 3Sum
// https://leetcode.com/problems/3sum/

var threeSum = function (nums) {
  const answer = [];
  // 정렬
  nums.sort((a, b) => a - b);
  // 하나의 elemet fix해서 합이 0이 되는 두 element 탐색
  for (let i = 0; i < nums.length - 2; i++) {
    // 중복된 element skip
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    // left, right index 설정
    let left = i + 1;
    let right = nums.length - 1;

    // 양 쪽(left, right)에서 탐색
    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];
      if (sum === 0) {
        answer.push([nums[i], nums[left], nums[right]]);
        left++; // 중복되는 elemet skip하면서 새로운 left 설정
        while (left < right && nums[left] === nums[left - 1]) left++;
        continue;
      } else if (sum > 0) right--;
      else left++;
    }
  }

  return answer;
};
