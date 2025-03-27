function mostFrequentDigitSum(n) {
    let result = n;
    const digitsSumArr = [];

    while(result !== 0){
      let digitsSum = 0;
      const strN = String(result);

      for(let i = 0; i < strN.length; i++){
        digitsSum += parseInt(strN[i]);
      }

      result -= digitsSum;

      digitsSumArr.push(digitsSum);
    }

    const frequency = {};
    let maxFrequency = 0;
    let mostFrequent = null;
    
    for(let i = 0; i < digitsSumArr.length; i++) {
      const num = digitsSumArr[i];
      frequency[num] = (frequency[num] || 0) + 1;

      if(frequency[num] > maxFrequency) {
        maxFrequency = frequency[num];
        mostFrequent = num;
      }
    }
  
    return mostFrequent;
  }
  