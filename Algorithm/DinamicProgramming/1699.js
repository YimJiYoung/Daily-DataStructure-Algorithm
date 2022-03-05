// 제곱수의 합
// https://www.acmicpc.net/problem/1699

const fs = require('fs');
const N = Number(fs.readFileSync('/dev/stdin').toString());
// minSquareNumTermCount[i] : 제곱수들의 합으로 표현할 때에 그 항의 최소 개수
const minSquareNumTermCount = new Array(N + 1).fill(Infinity);
const squareNums = [];

for (let i = 1; i <= N; i++) {
    const squareRoot = Math.sqrt(i);
    if (parseInt(squareRoot) === squareRoot) {
        minSquareNumTermCount[i] = 1;
        squareNums.push(i);
        continue;
    }
    
    for (let squreNum of squareNums) {
        minSquareNumTermCount[i] = Math.min(minSquareNumTermCount[i], 1 + minSquareNumTermCount[i - squreNum]);
    }
}

console.log(minSquareNumTermCount[N]);