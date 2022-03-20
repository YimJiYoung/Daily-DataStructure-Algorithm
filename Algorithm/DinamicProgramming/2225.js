// 합분해
// https://www.acmicpc.net/problem/2225

const fs = require('fs');
const [N, K] = fs.readFileSync('/dev/stdin').toString().split(' ').map(Number);
// caseNums[N][K]: 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수 
const caseNums = Array.from({ length: N + 1 }, () => new Array(K + 1).fill(0));

for (let n = 0; n <= N; n++) {
    caseNums[n][1] = 1;
}

for (let k = 2; k <= K; k++) {
    for (let n = 0; n <= N; n ++) {
        caseNums[n][k] += caseNums[n][k - 1];
        if (n > 0) {
            caseNums[n][k] += caseNums[n - 1][k];
        } 
        caseNums[n][k] %= 1000000000;
    }
}


console.log(caseNums[N][K]);