var duplicateZeros = function(arr) {
    let zeroCount = 0;
    let length =  arr.length;
    let index = 0;
    
    // 2번씩 반복될 0의 숫자(zeroCount) 계산
    while(index < length) {
        if (arr[index] === 0) {
            // 새로운 배열의 마지막 요소가 0인 경우 
            // 이 0의 중복은 배열에 포함되지 않으므로 zeroCount에서 제외하고 배열의 마지막 요소로 넣는다.
            if(index === length - 1) {
                arr[arr.length - 1] = 0;
                length--;
                break;
            }
            zeroCount++;
            length--;
        }
        index++;
    }
    
    index = length - 1;

    while (index >= 0) {
        if (arr[index] === 0) {
            arr[index + zeroCount] = 0;
            zeroCount -= 1;
        }
        arr[index + zeroCount] = arr[index];
        index--;
    }
};