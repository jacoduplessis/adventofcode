const fs = require('fs')

const DAY = 1

const input = fs.readFileSync(__dirname + `/input/${DAY}.txt`, 'utf8').trim()

function getCaptcha(s, halfway=false) {
  const nums = s.split('').map(n => parseInt(n))
  const N = nums.length
  const step = halfway ? N/2 : 1
  return nums.reduce((acc, n, i) => acc + (nums[i] === nums[(i + step) % N] ? nums[i] : 0), 0)
}

console.log(getCaptcha(input))
console.log(getCaptcha(input, true))