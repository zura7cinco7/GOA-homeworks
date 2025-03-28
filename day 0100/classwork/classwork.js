function manualFindIndex(arr, callback) {
    for (let i = 0; i < arr.length; i++) {
      if (callback(arr[i], i, arr)) {
        return i;
      }
    }
    return -1;
  }

  let arr = [10, 20, 30, 40, 50];
  let index = manualFindIndex(arr, function(element) {
    return element === 30; 
  });
  
  console.log(index); 
  