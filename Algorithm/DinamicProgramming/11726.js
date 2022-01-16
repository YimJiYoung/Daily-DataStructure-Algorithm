// 2×n 타일링
// https://www.acmicpc.net/problem/11726

const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString());
const caseNums = new Array(n + 1).fill(0);
caseNums[1] = 1;
caseNums[2] = 2;

for (let i = 3; i <= n; i++) {
    // 1x2 타일을 놓았을 때의 경우의 수(caseNums[i - 1]) + 2x1 타일을 놓았을 때의 경우의 수(caseNums[i - 2])
    caseNums[i] = caseNums[i - 1] + caseNums[i - 2];
    caseNums[i] %= 10007;
}

console.log(caseNums[n]);