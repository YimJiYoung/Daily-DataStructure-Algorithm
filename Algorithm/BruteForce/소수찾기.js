function canMake(numbers, target) {
  // numbers의 숫자로 target 만들 수 있는지 판별
  target = target.toString().split("");
  const numCount = new Array(10).fill(0);
  for (let num of numbers) {
    numCount[num]++;
  }
  for (let num of target) {
    if (--numCount[num] < 0) return false;
  }
  return true;
}

function solution(numbers) {
  let answer = 0;
  const maxNum = Math.pow(10, numbers.length);

  // 소수 판별 배열 - 에라토스테네스의 체
  const isPrime = new Array(maxNum).fill(true);
  isPrime[0] = isPrime[1] = false;
  for (let i = 2; i <= Math.sqrt(maxNum); i++) {
    if (isPrime[i]) {
      let j = 2;
      while (i * j <= maxNum) {
        isPrime[i * j++] = false;
      }
    }
  }

  for (let i = 2; i <= maxNum; i++) {
    // 소수이면서 numbers로 만들 수 있는 숫자인 경우 count 증가
    if (isPrime[i] && canMake(numbers, i)) {
      answer++;
    }
  }

  return answer;
}
