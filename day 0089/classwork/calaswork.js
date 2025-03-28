const zuka = (name, age) => {
    if (age >= 18) {
        return name + "შესვლა შეგიძლია";
    } else {
        return name + "ვერშეხვალ";
    }
};

const name1 = prompt("შეიყვანე შენი სახელი");
const age1 = prompt("შეიყვანე შენი ასაკი");

console.log(zuka(name1, Number(age1)));
