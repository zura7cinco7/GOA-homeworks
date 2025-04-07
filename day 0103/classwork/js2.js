const original = { name: "Alice" };

function modify(obj) {
  obj.name = "Bob";
}

modify(original);

console.log(original.name); 
