function average(a, b, c, d, e) {
    return (a + b + c + d + e) / 5;
}

console.log(average(10, 20, 30, 40, 50));
       

const averageArrow = (a, b, c, d, e) => (a + b + c + d + e) / 5;

console.log(averageArrow(10, 20, 30, 40, 50)); 


function greetUser() {
    let firstName = prompt("Enter your first name:");
    let lastName = prompt("Enter your last name:");
    let age = prompt("Enter your age:");
    
    console.log(`Hello, ${firstName} ${lastName}! You are ${age} years old.`);
}

greetUser();


const calculateTotal = (price, quantity = 1) => price * quantity;

console.log(calculateTotal(20, 3)); 
console.log(calculateTotal(15));  
  

function testScope() {
    let myVariable = "Inside function";
    console.log(myVariable);
}

testScope();
console.log(myVariable); 


function testScopeVar() {
    var myVariable = "Inside function";
    console.log(myVariable);
}

testScopeVar();
console.log(myVariable); 
