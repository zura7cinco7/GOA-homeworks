const names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"];

const filteredNames = names.filter((name, index) => index % 2 === 0);

console.log(filteredNames); // ["Alice", "Charlie", "Eve"]
