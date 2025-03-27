function isEven(num) {
    return num % 2 === 0;
  }
  function executeFunction(callback) {
    let result = callback(4); 
    console.log(result); 
  }

  executeFunction(isEven);
  