// 가장 긴 증가하는 부분 수열
// https://www.acmicpc.net/problem/11053

const fs = require('fs');
const lines = fs.readFileSync('/dev/stdin').toString().split('\n');
const N = Number(lines[0]);
const arr = lines[1].split(' ').map(Number);
// LDS(Longest Decreasing Subsequence)
// LDSLengthOf[i] =  i번째 원소를 마지막으로 하는 LDS의 길이
const LDSLengthOf = new Array(N).fill(0);
let LDS = 0;

for (let i = 0; i < N; i++) {
    // 0 ~ i - 1까지의 원소들에서, i번째 원소보다 값이 큰 것들 중, 가장 큰 LDSLengthOf 값
    let possiblePrevLDS = 0;
    for (let j = 0; j < i; j++) {
        if (arr[i] < arr[j]) {
            possiblePrevLDS = Math.max(LDSLengthOf[j], possiblePrevLDS);
        }
    }

    LDSLengthOf[i] = possiblePrevLDS + 1;
    LDS = Math.max(LDS, LDSLengthOf[i])
}

console.log(LDS);
