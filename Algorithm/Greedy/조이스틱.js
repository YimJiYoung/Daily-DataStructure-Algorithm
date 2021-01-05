// 조이스틱
// https://programmers.co.kr/learn/courses/30/lessons/42860

function findClosestIndex(curIndex, name, length) {
  // 가장 가까운 위치에 있는 index와 거리 반환
  if (name.length === 0) return [-1, 0];
  let minMove = [-1, 1000000];
  for (let nextIndex = 0; nextIndex < name.length; nextIndex++) {
    let [char, index] = name[nextIndex];
    const moveCount = Math.min(
      Math.abs(index - curIndex), // 바로 가는 경우
      curIndex < index ? curIndex + length - index : index + length - curIndex // 한바퀴 돌아가는 경우
    );
    if (moveCount < minMove[1]) {
      minMove = [nextIndex, moveCount];
    }
  }
  return minMove;
}

function solution(name) {
  let count = 0;
  const A = "A".charCodeAt(0);
  const Z = "Z".charCodeAt(0);
  let nameLength = name.length;

  name = name // A가 아닌 문제 제거하고 원래 index와 함께 저장 - [문자, 원래 인덱스]
    .split("")
    .map((v, i) => [v, i])
    .filter((x) => x[0] !== "A");

  let curIndex = 0;
  if (name[0][1] !== 0) {
    // A가 아닌 첫 문자의 위치가 첫 번째가 아닐 때 - 해당 위치까지 가는 moveCount 계산
    count += Math.min(name[0][1], nameLength - name[0][1]);
  }

  while (name.length > 0) {
    // 가까운 위치의 문자 하나씩 탐색하면서 처리
    let [char, index] = name[curIndex];
    const code = char.charCodeAt(0);
    const upDownCount =
      Math.abs(code - A) < Math.abs(code - Z)
        ? Math.abs(code - A)
        : Math.abs(code - Z) + 1;
    count += upDownCount;

    name.splice(curIndex, 1); // 처리된 문자 제거

    const [nextIndex, moveCount] = findClosestIndex(index, name, nameLength); // 가장 가까운 위치에 있는 인덱스, 거리 구하기
    count += moveCount;

    if (nextIndex === -1) break;
    curIndex = nextIndex;
  }

  return count;
}

console.log(solution("ABABAAAAABA"));
