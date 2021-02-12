function solution(N, stages) {
    const failRates = [];
    
    stages.sort((a, b) => a - b);
    let length = stages.length;
    let index = 0; // stages 탐색할 index
    
    // 스테이지 별로 실패율 계산
    for (let stage = 1; stage <= N; stage++) {
        if (length === 0 || index >= stages.length) {
            failRates.push([0, stage]);
            continue;
        }
        
        let failCount = 0;
        while (stages[index] === stage)  {
            index++;
            failCount++;
        }
       
        failRates.push([failCount / length, stage]);
        length -= failCount;
    }
 
    return failRates.sort((a, b) => {
        if (a[0] - b[0] !== 0)
            return b[0] - a[0];
        return a[1] - b[1];
    }).map((x) => x[1]);;
}