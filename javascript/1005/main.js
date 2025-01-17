var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

function averageOne() {
  var a = parseFloat(lines[0]);
  var b = parseFloat(lines[1]);

  var weightOfA = 3.5;
  var weightOfB = 7.5;

  var media = (a * weightOfA + b * weightOfB) / (weightOfA + weightOfB);

  return `MEDIA = ${media.toFixed(5)}`;
}

console.log(averageOne());
