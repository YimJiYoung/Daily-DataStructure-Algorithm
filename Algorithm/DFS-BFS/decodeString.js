// Decode String
// https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1379/

var decodeString = function(s) {
    const stack = [];
    let curStr = '';
    let curNum = 0; // 반복 횟수 (1 ~ 300)
    
    for (let token of s) {
        if (Number.isInteger(+token)) {
            curNum = curNum*10 + +token;
        }
        else if (token === '[') { 
            // 현재 문자열과 반복 횟수 stack에 push
            stack.push(curStr);
            stack.push(curNum);
            curStr = '';
            curNum = 0;
        }
        else if (token === ']') { 
            // 이전 문자열과 반복 횟수로 현재 문자열 업데이트 
            const num = stack.pop();
            const prevStr = stack.pop();
            curStr = prevStr + curStr.repeat(num);
        }
        else {
            curStr += token;
        }
    }
    
    return curStr;
};