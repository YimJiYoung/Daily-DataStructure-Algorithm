// 모의고사
// https://programmers.co.kr/learn/courses/30/lessons/42840?language=javascript

function solution(answers) {
  const scores = [0, 0, 0];
  const patterns = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
  ];
  const result = [];

  for (let i = 0; i < answers.length; i++) {
    for (let j = 0; j < patterns.length; j++) {
      if (answers[i] === patterns[j][i % patterns[j].length]) scores[j]++;
    }
  }

  const maxScore = Math.max(...scores);

  for (let i = 0; i < scores.length; i++) {
    if (scores[i] === maxScore) result.push(i + 1);
  }

  return result;
}

console.log(solution([1, 3, 2, 4, 2]));
