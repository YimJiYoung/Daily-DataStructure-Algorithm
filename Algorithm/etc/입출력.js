const fs = require('fs');
const lines = fs.readFileSync('/dev/stdin').toString().split('\n');

for (const line of lines) {
    if (line === '') return;
    const [a, b] = line.split(' ');
    console.log(Number(a) + Number(b));
}


const fs = require('fs');
const word = fs.readFileSync('/dev/stdin').toString();
let turn = 0;

// 11721
const fs = require('fs');
const word = fs.readFileSync('/dev/stdin').toString();
let turn = 0;

while(true) {
    const slicedWord = word.slice(turn, turn + 10);
    console.log(slicedWord);
    if (slicedWord.length < 10) break;
    turn += 10;
}

// 2741
const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString());

console.log(Array.from({ length: n }, (_, index) => index + 1).join('\n'));

// 2742
const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString());

console.log(Array.from({ length: n }, (_, index) => n - index).join('\n'));

// 2739
const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString());
let result = '';

for (let i = 1; i <= 9; i++) {
    result += `${n} * ${i} = ${n*i}\n`;
}

console.log(result);

// 1924
const fs = require('fs');
const [x, y] = fs.readFileSync('/dev/stdin').toString().split(' ').map(Number);

const daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
const nameOfDays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'];
const dayDiff = daysOfMonth.slice(0, x - 1).reduce((sum, cur) => sum + cur, 0) + (y - 1);
console.log(nameOfDays[dayDiff % 7]);


// 10818
const fs = require('fs');
const lines = fs.readFileSync('/dev/stdin').toString().split('\n');
const numbers = lines[1].split(' ').map(Number);
let maxNum = -1000000;
let minNum = 1000000;

for (const number of numbers) {
    if (number > maxNum) {
        maxNum = number;
    }
    if (number < minNum) {
        minNum = number;
    }
}

console.log(`${minNum} ${maxNum}`)


// 2439
const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString());
let result = '';

for (let i = 1; i <= n; i++) {
    result += ' '.repeat(n - i) + '*'.repeat(i) + '\n';
}

console.log(result);

// 2440
const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString());
let result = '';

for (let i = n; i > 0; i--) {
    result += '*'.repeat(i) + '\n';
}

console.log(result);

// 2441
const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString());
let result = '';

for (let i = n; i > 0; i--) {
    result += ' '.repeat(n - i) + '*'.repeat(i) + '\n';
}

console.log(result);

// 2442
const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString());
let result = '';

for (let i = 1; i <= n; i++) {
    result += ' '.repeat(n - i) + '*'.repeat(2*i - 1);
    if (i !== n) {
        result += '\n';
    }
}

console.log(result);

// 2445
const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString());
let result = '';

for (let i = 1; i <= n; i++) {
    result += '*'.repeat(i) + ' '.repeat(2*n - 2*i) +'*'.repeat(i) +'\n';
}

for (let i = n - 1; i > 0; i--) {
    result += '*'.repeat(i) + ' '.repeat(2*n - 2*i) +'*'.repeat(i) + '\n';
}

console.log(result);

// 2552
const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString());
let result = '';

for (let i = 1; i <= n; i++) {
    result += ' '.repeat(n - i) +'*'.repeat(i) +'\n';
}

for (let i = n - 1; i > 0; i--) {
    result += ' '.repeat(n - i) +'*'.repeat(i) +'\n';
}

console.log(result);

//2446
const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString());
let result = '';

for (let i = n; i > 0; i--) {
    result += ' '.repeat(n - i) + '*'.repeat(2*i - 1) + '\n';
}

for (let i = 2; i <= n; i++) {
    result += ' '.repeat(n - i) + '*'.repeat(2*i - 1) + '\n';
}

console.log(result);

// 10991
const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString());
let result = '';

for (let i = 1; i <= n; i++) {
    result += ' '.repeat(n - i);
    for (let j = 0; j < i; j ++) {
        if (j !== i - 1) {
            result += '* ';
        }
        else {
            result += '*'
        }
    }
    result += '\n'
}

console.log(result);

// 10992
const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString());
let result = '';

for (let i = 1; i <= n; i++) {
    if (i === 1) {
        result += ' '.repeat(n - i) + '*' + '\n';
    } 
    else if (i === n) {
        result += '*'.repeat(2*n - 1);
    }
    else {
        result += ' '.repeat(n - i) + '*' + ' '.repeat(2*i - 3) + '*' + '\n';
    }
}

console.log(result);

