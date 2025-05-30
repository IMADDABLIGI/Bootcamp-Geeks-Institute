const test = () => {
    console.log("Starting Test");
    return (
        new Promise((resolve) => {
            console.log("Inside Promise");
            setTimeout(() => {
                console.log("Finished Waiting...");
                resolve("Finished");
            }, 2000)
            }
        )
    )
}

test().then( () =>
    console.log("After Test")
)