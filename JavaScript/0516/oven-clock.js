// https://www.acmicpc.net/problem/2525

// JS 입출력 방법
const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");

let currentTime = input[0].split(" ").map((x) => +x); // 현재 시간 & 분 을 나누기 위해서
let startHour = currentTime[0]; // 현재 시간을 구한다
let startMin = currentTime[1]; // 현재 분을 구한다
let taken = input[1]; // 인풋의 2번쨰 줄 (걸리는 시간)
const takenHour = Math.floor(+taken / 60); // 걸리는 시간을 쪼개고
const takenMin = +taken % 60; // 걸리는 시간의 분도 쪼개고
let endHour = startHour + takenHour;
let endMin;

if (startMin + takenMin >= 60) {
  endHour++;
  endMin = startMin + takenMin - 60;
} else if (startMin + takenMin < 60) {
  endMin = startMin + takenMin;
}

if (endHour >= 24) {
  endHour -= 24;
}

console.log(endHour, endMin);
