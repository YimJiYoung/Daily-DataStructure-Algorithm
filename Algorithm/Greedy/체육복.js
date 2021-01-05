function solution(n, lost, reserve) {
  const reserved = new Array(n + 1).fill(false);

  for (let stud of reserve) {
    reserved[stud] = true;

    let lostedIdx = lost.indexOf(stud);
    // 여분 갖고 있는 사람이 잊어 버린 경우
    if (lostedIdx !== -1) {
      lost.splice(lostedIdx, 1);
      reserved[stud] = false;
    }
  }

  let count = n - lost.length;

  for (let stud of lost) {
    if (stud > 0 && reserved[stud - 1]) {
      reserved[stud - 1] = false;
      count++;
    } else if (stud < n && reserved[stud + 1]) {
      reserved[stud + 1] = false;
      count++;
    }
  }

  return count;
}
