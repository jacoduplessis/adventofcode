const fs = require('fs')

const DAY = 2

const input = fs.readFileSync(__dirname + `/input/${DAY}.txt`, 'utf8').trim()

function getChecksum(s) {
  return s.split('\n').reduce((acc, line) => {
    const nums = line.split('\t').map(s => parseInt(s)).sort((a, b) => a - b)
    return acc + nums[nums.length - 1] - nums[0]
  }, 0)
}

function getDivision(s) {
  return s.split('\n').reduce((acc, line) => {
    const nums = line.split('\t').map(s => parseInt(s)).sort((a, b) => a - b)

    function getResult(x) {
      for (let i = 0; i < x.length; i++) {
        for (let j = 0; j < x.length; j++) {
          if (i !== j && x[i] % x[j] === 0) {
            return x[i] / x[j]
          }
        }
      }
    }

    return acc + getResult(nums)
  }, 0)
}

console.log("PART 1", getChecksum(input))
console.log("PART 2", getDivision(input))