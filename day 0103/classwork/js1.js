const personAges = {
    Alice: 25,
    Bob: 30,
    Charlie: 35
  };
  const doubledAges = manualMapObj(personAges, (value, key) => value * 2);
  
  console.log(doubledAges);
  