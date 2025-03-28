function zuka(name) {  // ფუნქცია იღებს name-ს პარამეტრად
    console.log("გამარჯობა, " + name); // დაბეჭდავს გამარჯობას
}

zuka("zuka");  // გამოვიძახეთ ფუნქცია "zuka"



let zuka1 = 10;  // გლობალური ცვლადი

function zura() {
    let zuka1 = 5;  // ლოკალური ცვლადი
    console.log("ლოკალური", zuka1);  
}

myFunction(); 
console.log("გლობალური", zuka1);  