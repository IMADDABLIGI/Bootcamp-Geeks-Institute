function showProps(obj, objName) {
  let result = '';
  for (let i in obj) {
    // obj.hasOwnProperty() is used to filter out properties from the object's prototype chain
    if (obj.hasOwnProperty(i)) {
      result += `${objName}.${i} = ${obj[i]}\n`;
    }
  }
  return result;
}


myCar.make = Ford
myCar.model = Mustang
myCar.year = 1969
showProps(myCar, "myCar")