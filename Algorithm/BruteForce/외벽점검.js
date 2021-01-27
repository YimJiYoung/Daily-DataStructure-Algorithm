// 외벽 점검
// https://programmers.co.kr/learn/courses/30/lessons/60062?language=javascript#

// 순열 계산 (참고: https://stackoverflow.com/questions/9960908/permutations-in-javascript?page=1&tab=votes#tab-top)
function permutator(inputArr) {
    var results = [];
  
    function permute(arr, memo) {
      var cur, memo = memo || [];
  
      for (var i = 0; i < arr.length; i++) {
        cur = arr.splice(i, 1);
        if (arr.length === 0) {
          results.push(memo.concat(cur));
        }
        permute(arr.slice(), memo.concat(cur));
        arr.splice(i, 0, cur[0]);
      }
  
      return results;
    }
  
    return permute(inputArr);
  }
  
  
  function solution(n, weak, dist) {
      let answer = Infinity;
      let weakLen = weak.length;
      
      // weak 길이 2배로 늘리기 (원형 데이터 처리하기 쉽도록)
      for (let i = 0; i < weakLen; i++) {
          weak.push(weak[i] + n);
      }
      
      const permutations = permutator(dist);
      
      // 시작점 선정
      for (let start = 0; start < weakLen; start++) {
          for (let friends of permutations) {
              let count = 1;
              let position = weak[start] + friends[count - 1];
              let isCovered = true;
              // 각 weak 지점에 대해 갈 수 있는지 확인 - 안되면 친구 더 투입
              for (let index = start; index < start + weakLen; index++) {
                  if (weak[index] > position) {
                      count += 1;
                      if (count > dist.length)  {
                          isCovered = false;
                          break;
                      }
                      position = weak[index] + friends[count - 1];
                  }
              }
              if (isCovered) answer = Math.min(answer, count);
          }
      }
      
      if (!isFinite(answer)) return -1;
      return answer;
  }