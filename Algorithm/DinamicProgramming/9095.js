// 1, 2, 3 더하기
// https://www.acmicpc.net/problem/9095

const fs = require('fs');
const [testCaseNum, ...nums] = fs.readFileSync('/dev/stdin').toString().split('\n').map(Number);
const caseNums = new Array(11).fill(0);
caseNums[1] = 1;
caseNums[2] = 2;
caseNums[3] = 4;

for (let i = 4; i < 11; i++) {
    caseNums[i] = caseNums[i - 1] + caseNums[i - 2] + caseNums[i - 3];
}

for (let t = 0; t < testCaseNum; t++) {
    console.log(caseNums[nums[t]]);
}