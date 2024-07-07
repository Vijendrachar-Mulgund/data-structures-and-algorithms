console.log("Hello from the JS File");

console.log("This parameter, ", this);

// Sum of all numbers up to 'n' / Traditional for Loop method
const sumUpto = (n) => {
  let total = 0;
  for (let i = 0; i <= n; i++) {
    total += i;
  }
  return total;
};

const startTime = performance.now();
const ans = sumUpto(1000000000);
const endTime = performance.now();
console.log(`Total Time Taken: for loop ${(endTime - startTime) / 1000} s`);
console.log(ans);

// Sum of all numbers up to 'n' / Using a mathematical formula

const sumUptoMath = (n) => {
  return (n * (n + 1)) / 2;
};

const startTimeMath = performance.now();
const ansMath = sumUptoMath(1000000000);
const endTimeMath = performance.now();
console.log(`Total Time Taken: Math Formula ${(endTimeMath - startTimeMath) / 1000} s`);
console.log(ansMath);
