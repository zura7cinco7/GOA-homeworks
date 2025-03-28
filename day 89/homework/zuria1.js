// Hoisting with function declarations
greet(); // ფუნქციის გამოძახება შესაძლებელია, რადგან ფუნქცია არის hoisted

function greet() {
    console.log('Hello, world!');
}

// Hoisting with var (variable declaration is hoisted, but not the value)
console.log(myVar); // undefined - ცვლადი hoisted-ია, მაგრამ ჯერ არ აქვს assigned value

var myVar = 'I am hoisted!';

console.log(myVar); // 'I am hoisted!' - ცვლადი მნიშვნელობა მიენიჭა, ახლა არის ხელმისაწვდომი

// Hoisting doesn't work with let and const the same way as var
// console.log(myLetVar); // Error: Cannot access 'myLetVar' before initialization
let myLetVar = 'This will throw an error';

// Function expression hoisting does not work
// myFunction(); // Error: myFunction is not a function

var myFunction = function() {
    console.log('This is a function expression!');
};
