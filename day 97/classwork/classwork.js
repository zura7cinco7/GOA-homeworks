function isEven(num) {
    return num % 2 === 0;
  }
    function manualFilter(arr, func) {
    let filteredArr = [];
    
    for (let i = 0; i < arr.length; i++) {
      if (func(arr[i])) {
        filteredArr.push(arr[i]);
      }
    }
        return filteredArr;
  }
  let numbers = [1, 2, 3, 4, 5, 6, 7, 8];
  let evenNumbers = manualFilter(numbers, isEven);
  console.log(evenNumbers); 
  