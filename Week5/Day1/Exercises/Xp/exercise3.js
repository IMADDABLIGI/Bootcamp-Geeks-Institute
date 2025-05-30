const obj1 = new Promise((resolve) => {
            resolve(3);
        })


const obj2 = new Promise((resolve, reject) => {
    reject("Boo!");
})

obj1.then((res)=> console.log(res));
obj2.catch((res)=> console.log(res));