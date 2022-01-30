// 이친수
// https://www.acmicpc.net/problem/2193

const fs = require('fs');
const N =  Number(fs.readFileSync('/dev/stdin').toString());
// pinaryNum[n][i] i로 끝나는 n자리 이친수의 개수
// 2^53 - 1보다 큰 정수를 표현할 수 있는 내장 객체인 BigInt를 사용해야 함
const pinaryNum = new Array(N).fill(null).map(() => new Array(2).fill(BigInt(0))); 

pinaryNum[0][1] = BigInt(1);

for (let n = 1; n < N; n++) {
  // 0 앞에는 0과 1이 올 수 있다.
  pinaryNum[n][0] = pinaryNum[n - 1][0] + pinaryNum[n - 1][1]; 
  // 1 앞에는 0만 올 수 있다. (1이 두번 연속으로 나올 수 없음)
  pinaryNum[n][1] = pinaryNum[n - 1][0];
}

console.log((pinaryNum[N - 1][0] + pinaryNum[N - 1][1]).toString());
