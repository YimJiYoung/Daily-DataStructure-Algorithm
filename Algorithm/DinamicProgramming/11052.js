// 카드 구매하기
// https://www.acmicpc.net/problem/11052

const fs = require('fs');
const [N, line] = fs.readFileSync('/dev/stdin').toString().split('\n');
const cardCosts = line.split(' ').map(Number);
const maxCostForCards = [...cardCosts];

for (let i = 1; i < N; i++) {
    for (let j = 0; j <= i / 2 ; j++) {
        maxCostForCards[i] = Math.max(cardCosts[j] + maxCostForCards[i - (j + 1)], maxCostForCards[i]);
    }
}

console.log(maxCostForCards[N - 1]);