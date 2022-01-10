// 1로 만들기
// https://www.acmicpc.net/problem/1463

const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString());
const minOperationCounts = new Array(n).fill(Infinity);
minOperationCounts[1] = 0;

for (let i = 2; i <= n; i++) {
    let minCount = Infinity;
    if (i % 2 === 0) {
        minCount = Math.min(minCount, minOperationCounts[i / 2] + 1);
    }
    if (i % 3 === 0) {
        minCount = Math.min(minCount, minOperationCounts[i / 3] + 1);
    }
    minOperationCounts[i] = Math.min(minCount, minOperationCounts[i - 1] + 1);
}

console.log(minOperationCounts[n]);