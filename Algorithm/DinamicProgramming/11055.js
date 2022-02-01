// 가장 큰 증가 부분 수열
// https://www.acmicpc.net/problem/11055

const fs = require('fs');
const lines = fs.readFileSync('/dev/stdin').toString().split('\n');
const N = Number(lines[0]);
const arr = lines[1].split(' ').map(Number);
// LIS(Largest Increasing Subsequence)
// LISLengthOf[i] =  i번째 원소를 마지막으로 하는 LIS의 길이
const LISLengthOf = new Array(N).fill(0);
let LIS = 0;

for (let i = 0; i < N; i++) {
    // 0 ~ i - 1까지의 원소들에서, i번째 원소보다 값이 작은것들 중, 가장 큰 LISLengthOf 값
    let possiblePrevLIS = 0;
    for (let j = 0; j < i; j++) {
        if (arr[i] > arr[j]) {
            possiblePrevLIS = Math.max(LISLengthOf[j], possiblePrevLIS);
        }
    }

    LISLengthOf[i] = possiblePrevLIS + arr[i];
    LIS = Math.max(LIS, LISLengthOf[i]);
}

console.log(LIS);