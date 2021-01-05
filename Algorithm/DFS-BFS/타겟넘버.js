// 타겟넘버
// https://programmers.co.kr/learn/courses/30/lessons/43165

function solution(numbers, target) {
  var answer = 0;
  return getAllCase(target, 0, numbers);
}

// i부터 numbers를 조회했을때 target이 만들어지는 경우의 수
function getAllCase(target, i, numbers) {
  // i가 마지막 index가 되고 target이 0이면 target number가 만들어지는 경우의 수이다
  if (i === numbers.length) return target === 0 ? 1 : 0;
  return (
    getAllCase(target - numbers[i], i + 1, numbers) +
    getAllCase(target + numbers[i], i + 1, numbers)
  );
}
