function solution(lines) {
  let answer = 0;
  let arr = Array.from({ length: 200 }, (undefined, i) => 0);

  for (const init of lines) {
    for (let j = init[0] + 100; j < init[1] + 100; j++) {
      arr[j] += 1;
    }
  }

  for (const value of arr) {
    if (value > 1) {
      answer += 1;
    }
  }

  return answer;
}
