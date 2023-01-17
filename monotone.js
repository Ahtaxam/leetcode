var minFlipsMonoIncr = function (s) {
  let countOne = 0;
  let countZero = 0;
  let res = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] == 1) {
      countOne++;
    } else {
      countZero = Math.min(countZero + 1, countOne);
    }
  }
  return countZero;
};

let s = "00001010000";
console.log(minFlipsMonoIncr(s));

// Example 1:
// Input: s = "00110"
// Output: 1
// Explanation: We flip the last digit to get 00111.

// Example 2:
// Input: s = "010110"
// Output: 2
// Explanation: We flip to get 011111, or alternatively 000111.

// Example 3:
// Input: s = "00011000"
// Output: 2
// Explanation: We flip to get 00000000.
