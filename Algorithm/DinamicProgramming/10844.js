// 쉬운 계단 수
// https://www.acmicpc.net/problem/10844

const fs = require('fs');
const N = Number(fs.readFileSync('/dev/stdin').toString());
const stepNum = new Array(N).fill(null).map(() => new Array(10).fill(0)); // stepNum[n][i] i로 시작하는 n 자리 수의 계단수의 개수

for (let i = 0; i < 10; i++) {
    stepNum[0][i] = 1;
}

for (let n = 1; n < N; n++) {
    for (let i = 0; i < 10; i++) {
        if (i > 0) {
            stepNum[n][i] += stepNum[n - 1][i - 1];
        }
        if (i < 9) {
            stepNum[n][i] += stepNum[n - 1][i + 1];
        }
        stepNum[n][i] %= 1000000000
    }
}

console.log(stepNum[N - 1].slice(1).reduce((sum, val) => sum + val) % 1000000000);