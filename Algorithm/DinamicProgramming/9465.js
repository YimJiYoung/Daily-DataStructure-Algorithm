// 스티커
// https://www.acmicpc.net/problem/2193

const fs = require('fs');
const [T, ...lines] = fs.readFileSync('/dev/stdin').toString().split('\n');

for (let t = 0; t < Number(T); t++) {
  const N = Number(lines[3 * t]);
  const sticker = lines.slice(3 * t + 1, 3 * t + 3).map(line => line.split(' ').map(Number));
  // maxStickerSum[n][i] : n열 i행에 위치한 스티커를 선택했을 때의 n열부터 시작하는 스티커 배열에서의 최대 점수
  const maxStickerSum = new Array(N + 1).fill(null).map(() => new Array(2).fill(0)); 
  maxStickerSum[N][0] = 0;
  maxStickerSum[N][1] = 0;
  maxStickerSum[N - 1][0] = sticker[0][N - 1];
  maxStickerSum[N - 1][1] = sticker[1][N - 1];

  for (let n = N - 2; n >= 0; n--) {
    // 첫번째 스티커를 선택한 경우 다음 열의 두번째 스티커를 선택하거나(maxStickerSum[n + 1][1]) 다음 열의 스티커를 선택하지 않는 경우(Math.max(maxStickerSum[n + 2][1], maxStickerSum[n + 2][0]), 다다음 행의 첫번째 두번쨰 스티커 둘다 선택 가능) 두 가지 중 최대의 점수를 선택한다.
    maxStickerSum[n][0] = sticker[0][n] + Math.max(maxStickerSum[n + 1][1], Math.max(maxStickerSum[n + 2][1], maxStickerSum[n + 2][0]));
    maxStickerSum[n][1] = sticker[1][n] + Math.max(maxStickerSum[n + 1][0], Math.max(maxStickerSum[n + 2][1], maxStickerSum[n + 2][0]));
  }

  console.log(Math.max(maxStickerSum[0][0], maxStickerSum[0][1]));
}

