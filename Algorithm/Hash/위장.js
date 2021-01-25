function solution(clothes) {
    let answer = 0;
    const map = new Map();
    // 종류 별로 의상 개수 저장
    for (let [name, type] of clothes) {
        let count = map.get(type);
        if (!count) count = 0;
        map.set(type, count + 1);
    }
    // 경우의 수 계산 
    for (let count of map.values()) {
        // (이전 경우의 수 * (현재 의상 수 + 1))
        answer += (answer + 1) * count;
    }
     
    return answer;
}