function changer(num) {
    return num * 2;
  }
  function manualMap(arr, changer) {
    let changedArr = [];
        for (let i = 0; i < arr.length; i++) {
      changedArr.push(changer(arr[i]));
    }
    
    return changedArr;
  }
  let numbers = [1, 2, 3, 4, 5];
  let doubledNumbers = manualMap(numbers, changer);
  console.log(doubledNumbers); 
  