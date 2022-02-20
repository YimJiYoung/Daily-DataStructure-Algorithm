const fs = require('fs');
const [N, ...steps] = fs.readFileSync('/dev/stdin').toString().split('\n').map(Number);

// maxScoreBy[n]: n번쨰 계단부터 밟고 시작했을 떄 얻을 수 있는 최대 점수
const maxScoreBy = new Array(N).fill(0);
maxScoreBy[N - 1] = steps[N - 1];
maxScoreBy[N - 2] = steps[N - 1] + steps[N - 2];
maxScoreBy[N - 3] = steps[N - 1] + steps[N - 3];
let maxScore = steps[0];

if (N == 2) {
    maxScore = maxScoreBy[N - 2];
}

if (N > 2) {
    maxScore = Math.max(maxScoreBy[N - 1], maxScoreBy[N - 2], maxScoreBy[N - 3]);
}

for (let i = N - 4; i >= 0; i--) {
    // 다음 계단(steps[i + 1])을 오르는 경우 
    // 다음 다음 계단(steps[i + 2])을 오르는 경우
    maxScoreBy[i] = steps[i] + Math.max(steps[i + 1] + maxScoreBy[i + 3], maxScoreBy[i + 2]);
    maxScore = Math.max(maxScore, maxScoreBy[i]);
}

console.log(maxScore);