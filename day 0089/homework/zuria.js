// Global Scope - ცვლადი მიღებული ხდება მთელი ფაილის მასშტაბით
let globalVar = 'I am in global scope';

function exampleFunction() {
    // Function Scope - ცვლადი მოქმედებს მხოლოდ ამ ფუნქციაში
    let functionVar = 'I am in function scope';
    
    console.log(globalVar); // გლობალური ცვლადი ხელმისაწვდომია ფუნქციის შიგნით
    console.log(functionVar); // ფუნქციის ცვლადი ხელმისაწვდომია ამ ფუნქციაში
}

exampleFunction();

console.log(globalVar); // გლობალური ცვლადი ხელმისაწვდომია კოდის ნებისმიერ ადგილას

// console.log(functionVar); // ფუნქციის ცვლადი არ არის ხელმისაწვდომი კოდის გარეთ, გამოიწვევს შეცდომას
