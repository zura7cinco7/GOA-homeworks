const alphabet = ["A", "B", "C", ..."", "Z"];

const symbols = alphabet.map((curValue, index) => `${curValue} - ${index + 1}`);

console.log(symbols);
