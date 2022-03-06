// 타일 채우기
// https://www.acmicpc.net/problem/2133

const fs = require('fs');
const N = Number(fs.readFileSync('/dev/stdin').toString());

if (N === 0 || N % 2 === 1) {
    console.log(0);
} else {
    const caseNums = new Array(N + 1).fill(0);
    caseNums[0] = 1;
    caseNums[2] = 3;

    for (let i = 4; i <= N; i += 2) {
        // 끝에 2X2 타일을 채우는 경우의 수 X 나머지 공간을 채우는 경우의 수
        caseNums[i] = caseNums[2] * caseNums[i - 2];
        for (let j = 4; j <= i; j += 2) {
            // 끝에 ㄱ, ㄴ 형태로 타일을 나열한 모양의 너비가 j인 경우 X 나머지 공간 채우는 경우의 수
            caseNums[i] += 2 * caseNums[i - j];
        }
    }

    console.log(caseNums[N]);
}

