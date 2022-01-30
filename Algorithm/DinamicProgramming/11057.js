const fs = require('fs');
const N = Number(fs.readFileSync('/dev/stdin').toString());
const acsendNum = new Array(N).fill(null).map(() => new Array(10).fill(0)); // acsendNum[n][i] i로 시작하는 n 자리 수의 오름수의 개수

for (let i = 0; i < 10; i++) {
    acsendNum[0][i] = 1;
}

for (let n = 1; n < N; n++) {
    for (let i = 0; i < 10; i++) {
        acsendNum[n][i] += acsendNum[n - 1].slice(i).reduce((sum, val) => sum + val) % 10007;
    }
}

console.log(acsendNum[N - 1].reduce((sum, val) => sum + val) % 10007);
