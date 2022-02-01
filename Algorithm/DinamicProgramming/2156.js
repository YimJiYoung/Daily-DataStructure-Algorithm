// 포도주 시식
// https://www.acmicpc.net/problem/2156

const fs = require('fs');
const [N, ...wines] = fs.readFileSync('/dev/stdin').toString().split('\n').map(Number);

// maxAmountWine[n] : n번째 줄부터 최대로 마실 수 있는 포도주의 양
const maxAmountWine = new Array(N + 2).fill(0);
wines.push(0);
wines.push(0);
maxAmountWine[N - 1] = wines[N - 1];


for (let n = N - 2; n >= 0; n--) {
    // max(n번째 포도주 마시지 않는 경우, n번째 마시고 n+1번째 마시지 않는 경우, n번째와 n+1번째 모두 마시는 경우)
    maxAmountWine[n] = Math.max(maxAmountWine[n + 1], wines[n] + maxAmountWine[n + 2], wines[n] + wines[n + 1] + maxAmountWine[n + 3]);
}

console.log(maxAmountWine[0]);

