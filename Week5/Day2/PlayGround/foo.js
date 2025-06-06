const foo = async () => {
   console.log("Hey")
   throw new Error("Ta ach kat5awar");
}

foo()
    .then((res) => console.log(res))
    .catch((err) => console.log(err.message));