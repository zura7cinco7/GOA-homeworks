const numbers = [1, 2, 3, 4, 5, 6, 7, 8];

const doubledOddIndices = numbers.map((num, index) => index % 2 !== 0 ? num * 2 : num);

console.log(doubledOddIndices);
