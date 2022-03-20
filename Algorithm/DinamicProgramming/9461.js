// 파도반 수열
// https://www.acmicpc.net/problem/9461

const fs = require('fs');
const [testCaseNum, ...numbers] = fs.readFileSync('/dev/stdin').toString().split('\n').map(Number);

const padovanSequence = new Array(100);
padovanSequence[0] = padovanSequence[1] = padovanSequence[2] = 1;
padovanSequence[3] = padovanSequence[4] = 2;

for (let i = 5; i <= 100; i++) {
    padovanSequence[i] = padovanSequence[i - 1] + padovanSequence[i - 5];
}

for (let t = 0; t < testCaseNum; t++) {
    console.log(padovanSequence[numbers[t] - 1]);
}