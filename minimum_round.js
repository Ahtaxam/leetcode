function mimimumRound(tasks) {
  const obj = {};
  let round = 0;

  // store frequencies of each task
  for (let i = 0; i < tasks.length; i++) {
    if (obj[tasks[i]]) {
      obj[tasks[i]]++;
    } else {
      obj[tasks[i]] = 1;
    }
  }

  // apply math
  for (let key in obj) {
    if (obj[key] <= 1) {
      return -1;
    }
    if (obj[key] === 2) {
      round += 1;
    }
    if (obj[key] >= 3) {
      round += Math.floor(obj[key] / 3);
      if (obj[key] % 3 >= 1) {
        round += 1;
      }
    }
  }

  return round;
}

tasks = [];
console.log(mimimumRound(tasks));

// Example 1:
// Input: tasks = [2,2,3,3,2,4,4,4,4,4]
// Output: 4
// Explanation: To complete all the tasks, a possible plan is:
// - In the first round, you complete 3 tasks of difficulty level 2.
// - In the second round, you complete 2 tasks of difficulty level 3.
// - In the third round, you complete 3 tasks of difficulty level 4.
// - In the fourth round, you complete 2 tasks of difficulty level 4.
// It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.

// Example 2:
// Input: tasks = [2,3,3]
// Output: -1
// Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level.
// Hence, you cannot complete all the tasks, and the answer is -1.
