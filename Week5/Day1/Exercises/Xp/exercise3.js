const obj1 = Promise.resolve(3)

const obj2 = Promise.reject("Boo!")


obj1.then((res)=> console.log(res));
obj2.catch((res)=> console.log(res));