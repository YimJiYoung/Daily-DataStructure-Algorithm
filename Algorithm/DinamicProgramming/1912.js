// 연속합
// https://www.acmicpc.net/problem/1912

const fs = require('fs');
const lines = fs.readFileSync('/dev/stdin').toString().split('\n');
const N = Number(lines[0]);
const arr = lines[1].split(' ').map(Number);
// maxSeqSum[n] : n번째 요소를 마지막으로 갖도록 선택된 부분 수열의 가장 큰 합
const maxSeqSum = new Array(N); 
maxSeqSum[0] = arr[0];
let maxSum = arr[0];

for (let i = 1; i < N; i++) {
    maxSeqSum[i] = Math.max(arr[i], maxSeqSum[i - 1] + arr[i]);
    maxSum = Math.max(maxSum, maxSeqSum[i]);
}

console.log(maxSum);
