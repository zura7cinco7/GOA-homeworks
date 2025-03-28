function manualForEach(arr, func) {
    for (let i = 0; i < arr.length; i++) {
      func(arr[i]);
    }
  }
  let numbers = [1, 2, 3, 4, 5];
  function printNumber(num) {
    console.log(num);
  }
  manualForEach(numbers, printNumber);
