// 구명보트
// https://programmers.co.kr/learn/courses/30/lessons/42885

function solution(people, limit) {
  let count = 0;
  let start = 0;
  let end = people.length - 1;

  people.sort((a, b) => b - a); // 내림차순 정렬

  while (start < end) {
    // 가장 무거운 사람 + 가벼운 사람 조합 limit 초과 시 -> 무거운 사람만 태우기
    if (people[start] + people[end] > limit) start++;
    // limit 이내 -> 다음 조합 탐색
    else {
      start++;
      end--;
    }
    count++;
  }
  if (start === end) count++;

  return count;
}
