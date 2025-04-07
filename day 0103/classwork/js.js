function manualMapObj(obj, callback) {
    const newObj = {}; 
    for (let key in obj) {
      if (obj.hasOwnProperty(key)) {
        newObj[key] = callback(obj[key], key, obj);
      }
    }
  
    return newObj;
  }
  