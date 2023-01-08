var maxPoints = function (points) {
  let countXZero = 0;
  for (let i = 0; i < points.length; ++i) {
    if (points[i][0] === 0) {
      countXZero += 1;
    }
  }
  var max = 0;
  for (var i = 0; i < points.length; i++) {
    var map = {};
    var same = 1;
    for (var j = i + 1; j < points.length; j++) {
      if (points[i][0] === points[j][0] && points[i][1] === points[j][1]) {
        same++;
      } else {
        var slope =
          (points[i][1] - points[j][1]) / (points[i][0] - points[j][0]);
        map[slope] = map[slope] ? map[slope] + 1 : 1;
      }
    }
    var localMax = 0;
    for (var key in map) {
      localMax = Math.max(localMax, map[key]);
    }
    localMax += same;
    max = Math.max(max, localMax);
  }
  return countXZero > max ? countXZero:max
};

points = [
  [0, 1],
  [0, 0],
  [0, 4],
  [0, -2],
  [0, -1],
  [0, 3],
  [0, -4],
];

console.log(maxPoints(points));

// intuition:
// 1. find the slope between each point and the rest of the points and at beginning check that how many 
// points x axis are zero
// 2. store the slope in a map
// 3. find the max value in the map
// 4. return the max value


// Example 1:
// Input: points = [[1,1],[2,2],[3,3]]
// Output: 3

// Example 2:
// Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
// Output: 4
