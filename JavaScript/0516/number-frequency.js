// https://www.acmicpc.net/problem/14912
const input = require("fs").readFileSync("/dev/stdin").toString().split(" ");

const final = parseInt(input[0]);
const pick = parseInt(input[1]);
let pre = [];
let answer = 0;

for (let i = 1; i <= final; i++) {
  if (String(i).includes(pick.toString())) {
    pre.push(i);
  }
}

let digits = [];
for (let i = 0; i < pre.length; i++) {
  const numberString = String(pre[i]);
  digits = digits.concat(numberString.split(""));
}

for (let j = 0; j < digits.length; j++) {
  if (parseInt(digits[j]) === pick) {
    answer += 1;
  }
}

console.log(answer);

// 11 1
// 1 10 11 => 4
