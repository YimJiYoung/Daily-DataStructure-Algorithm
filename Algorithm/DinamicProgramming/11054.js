// 가장 긴 바이토닉 부분 수열
// https://www.acmicpc.net/problem/11053

const fs = require('fs');
const lines = fs.readFileSync('/dev/stdin').toString().split('\n');
const N = Number(lines[0]);
const arr = lines[1].split(' ').map(Number);
// LBSLengthOf[i][0] =  i번째 원소를 마지막으로 하는 증가하는 부분 수열의 최대 길이
// LBSLengthOf[i][1] =  i번째 원소를 마지막으로 하는 증가하다 감소하는 부분 수열의 최대 길이
const LBSLengthOf = Array.from({ length: N }).map(() => new Array(2).fill(1));
LBSLengthOf[0][0] = 1;
LBSLengthOf[0][1] = 1;
let LBS = 0;

for (let i = 0; i < N; i++) {
    let maxPrevLASofIndex = -1;
    let maxPrevLBSofIndex = -1;

    for (let j = 0; j < i; j++) {
        if (arr[i] > arr[j] && (maxPrevLASofIndex == -1 ||  LBSLengthOf[maxPrevLASofIndex][0] < LBSLengthOf[j][0])) {
            maxPrevLASofIndex = j;
            LBSLengthOf[i][0] = LBSLengthOf[maxPrevLASofIndex][0] + 1;
        }
        
        if (arr[i] < arr[j]) {
            if (maxPrevLBSofIndex == -1 || Math.max(LBSLengthOf[maxPrevLBSofIndex][0], LBSLengthOf[maxPrevLBSofIndex][1]) < Math.max(LBSLengthOf[j][0], LBSLengthOf[j][1])) {
                maxPrevLBSofIndex = j;
                LBSLengthOf[i][1] = Math.max(LBSLengthOf[maxPrevLBSofIndex][0], LBSLengthOf[maxPrevLBSofIndex][1]) + 1;
            }
        }
    }

    LBS = Math.max(LBS, LBSLengthOf[i][0], LBSLengthOf[i][1]);

}

console.log(LBS);