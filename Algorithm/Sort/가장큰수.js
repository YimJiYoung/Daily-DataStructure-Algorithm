// 가장 큰 수
// https://programmers.co.kr/learn/courses/30/lessons/42746?language=javascript

function compare(a, b) {
  // a, b 문자열로 변환하여 두 숫자를 합쳤을 때(a + b, b + a) 더 큰 쪽의 앞 숫자가 크다고 판단한다.
  a = a.toString();
  b = b.toString();
  return a + b - (b + a);
}

function solution(numbers) {
  let answer = "";
  numbers.sort(compare);

  while (numbers.length > 0) {
    const number = numbers.pop();
    answer += number.toString();
  }

  if (answer === "0".repeat(answer.length)) return "0";
  return answer;
}
